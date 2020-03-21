import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

def DataPreparation():
    spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
    data = spark.read.csv("Burnout_Data.csv",header=True, inferSchema=True)
    data = data.select('Tiempo_PlazaActual','EstadoCivil','Burnout_Antes','Hora_Social','Horas_Cuidados','Calorias','Peso','Contrato_Adjunto','Musica','Sexo','Estudias','Sales_Social','Edad','Estado_Animo','Tiempo_Vida_Laboral','Hijos','Lectura','Hora_Gratificante','Horas_Activ_Fisica')
    cols = data.columns

    from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
    categoricalColumns = ['Contrato_Adjunto','Musica','Sexo','Estudias','Sales_Social','Edad','Estado_Animo','Lectura','EstadoCivil']
    stages = []
    for categoricalCol in categoricalColumns:
        stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
        encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
        stages += [stringIndexer.setHandleInvalid("keep"), encoder]
    # Convert label into label indices using the StringIndexer
    label_stringIdx = StringIndexer(inputCol="Burnout_Antes", outputCol="label")
    stages += [label_stringIdx.setHandleInvalid("keep")]

    numericCols = ['Tiempo_PlazaActual','Hora_Social','Horas_Cuidados','Calorias','Peso','Tiempo_Vida_Laboral','Hijos','Hora_Gratificante','Horas_Activ_Fisica']
    assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
    assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
    stages += [assembler.setHandleInvalid("keep")]

    from pyspark.ml import Pipeline
    pipeline = Pipeline(stages = stages)
    pipelineModel = pipeline.fit(data)
    data = pipelineModel.transform(data)
    #path = 'modelo_Pipeline'
    #os.mkdir(path)
    #pipelineModel.save(os.path.join(path, 'Pipeline'))
    selectedCols = ['label', 'features'] + cols
    data = data.select(selectedCols)

    train, test = data.randomSplit([0.8, 0.2])
    print("Training Dataset Count: " + str(train.count()))
    print("Test Dataset Count: " + str(test.count()))
    return train,test

def LogisticRegression(train,test):
    from pyspark.ml.classification import LogisticRegression
    lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=1000,elasticNetParam=0.2,fitIntercept=False,threshold=1)
    lrModel = lr.fit(train)
    path = 'modelo_LogisticRegression'
    os.mkdir(path)
    lrModel.save(os.path.join(path, 'modelLogisticRegression'))

    predictions = lrModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10)

    from pyspark.ml.evaluation import BinaryClassificationEvaluator
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions))

def RandomForest(train,test):
    from pyspark.ml.classification import RandomForestClassifier
    rf = RandomForestClassifier(featuresCol='features', labelCol='label',numTrees=36,featureSubsetStrategy="all")
    rfModel = rf.fit(train)
    path = 'modelo_RandomForest'
    os.mkdir(path)
    rfModel.save(os.path.join(path, 'modelRandomForest'))
    predictions = rfModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10)

    from pyspark.ml.evaluation import BinaryClassificationEvaluator
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions))

def GradientBoostedTree(train,test):
    from pyspark.ml.classification import GBTClassifier
    gbt = GBTClassifier(maxIter=100,lossType="logistic",stepSize=0.99,featureSubsetStrategy='all')
    gbtModel = gbt.fit(train)
    path = 'modelo_GradientBoosted'
    os.mkdir(path)
    gbtModel.save(os.path.join(path, 'modelGradientBoosted'))
    predictions = gbtModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10)
    from pyspark.ml.evaluation import BinaryClassificationEvaluator
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions))

def Isotonic(train,test):
    from pyspark.ml.regression import IsotonicRegression
    iso = IsotonicRegression(featuresCol='features', labelCol='label')
    isoModel = iso.fit(train)
    path = 'modelo_IsotonicRegression'
    os.mkdir(path)
    isoModel.save(os.path.join(path, 'modelIsotonicRegression'))
    predictions = isoModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'prediction').show(10)


train,test = DataPreparation()
LogisticRegression(train,test)
RandomForest(train,test)
GradientBoostedTree(train,test)
Isotonic(train,test)








