import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

def DataPreparation():
    spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
    data = spark.read.csv("/Burnout_Data.csv",header=True, inferSchema=True)
    data = data.select('Tiempo_PlazaActual','EstadoCivil','Burnout_Antes','Hora_Social','Horas_Cuidados','Resting_HeartRate','Calorias','Frecuencia_Cardiaca_Minuto','Peso','Contrato_Adjunto','Musica','Sexo','Estudias','Sales_Social','Edad','Estado_Animo','Cantidad_Sueno_Profundo','Tiempo_Vida_Laboral','Hijos','Lectura','Minutos_Dormido')
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

    numericCols = ['Tiempo_PlazaActual','Hora_Social','Horas_Cuidados','Resting_HeartRate','Calorias','Frecuencia_Cardiaca_Minuto','Peso','Cantidad_Sueno_Profundo','Tiempo_Vida_Laboral','Hijos','Minutos_Dormido']
    assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
    assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
    stages += [assembler.setHandleInvalid("keep")]

    from pyspark.ml import Pipeline
    pipeline = Pipeline(stages = stages)
    pipelineModel = pipeline.fit(data)
    data = pipelineModel.transform(data)
    path = 'modelo_Pipeline'
    os.mkdir(path)
    pipelineModel.save(os.path.join(path, 'Pipeline'))
    selectedCols = ['label', 'features'] + cols
    data = data.select(selectedCols)

    train, test = data.randomSplit([0.7, 0.3])
    print("Training Dataset Count: " + str(train.count()))
    print("Test Dataset Count: " + str(test.count()))
    return train,test

def LogisticRegression(train,test):
    from pyspark.ml.classification import LogisticRegression
    lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=1000)
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
    rf = RandomForestClassifier(featuresCol='features', labelCol='label')
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
    gbt = GBTClassifier(maxIter=10)
    gbtModel = gbt.fit(train)
    predictions = gbtModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10)
    from pyspark.ml.evaluation import BinaryClassificationEvaluator
    evaluator = BinaryClassificationEvaluator()
    print("Test Area Under ROC: " + str(evaluator.evaluate(predictions, {evaluator.metricName: "areaUnderROC"})))
    from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
    paramGrid = (ParamGridBuilder()
                 .addGrid(gbt.maxDepth, [2, 4, 6])
                 .addGrid(gbt.maxBins, [20, 60])
                 .addGrid(gbt.maxIter, [10, 20])
                 .build())
    cv = CrossValidator(estimator=gbt, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)
    cvModel = cv.fit(train)
    path = 'modelo_GradientBoosted'
    os.mkdir(path)
    cvModel.save(os.path.join(path, 'modelGradientBoosted'))
    predictions = cvModel.transform(test)
    print('Test Area Under ROC', evaluator.evaluate(predictions))

def Perceptron(train,test):
    from pyspark.ml.classification import MultilayerPerceptronClassifier
    from pyspark.ml.evaluation import MulticlassClassificationEvaluator
    # create the trainer and set its parameters
    trainer = MultilayerPerceptronClassifier(maxIter=100, layers=None)
    # train the model
    model = trainer.fit(train)
    # compute accuracy on the test set
    result = model.transform(test)
    predictionAndLabels = result.select("prediction", "label")
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    path = 'modelo_Perceptron'
    os.mkdir(path)
    model.save(os.path.join(path, 'modelPerceptron'))
    print("Test set accuracy = " + str(evaluator.evaluate(predictionAndLabels)))


train,test = DataPreparation()
LogisticRegression(train,test)
RandomForest(train,test)
GradientBoostedTree(train,test)
Perceptron(train,test)








