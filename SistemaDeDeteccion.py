import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)


def DataPreparation():
    spark = SparkSession.builder.appName('SistemaDeDeteccion').master("local[*]").getOrCreate() #Creamos la sesión de spark
    data = spark.read.csv("Burnout_Data.csv",header=True, inferSchema=True) #Cargamos el dataset
    data = data.select('Tiempo_PlazaActual','EstadoCivil','Burnout_Antes','Hora_Social','Horas_Cuidados','Calorias','Peso','Contrato_Adjunto','Musica',
                'Sexo','Estudias','Sales_Social','Edad','Estado_Animo','Tiempo_Vida_Laboral','Hijos','Lectura','Hora_Gratificante','Horas_Activ_Fisica')
    #Nos quedamos con las columnas de importancia p>1 según el análisis de componentes
    cols = data.columns #Guardamos en una variable los nombres de las columnas

    from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler #importamos las librerias necesiarias para convertir datos categóricos
                                                                                        # en datos tratables por los algoritmos, es decir transformandolos a números
    categoricalColumns = ['Contrato_Adjunto','Musica','Sexo','Estudias','Sales_Social','Edad','Estado_Animo','Lectura','EstadoCivil']
    stages = [] #en esta variable guardaremos cada uno de los pasos para luego aplicarlos en el PipeLine
    for categoricalCol in categoricalColumns: #indexamos para cada una de las variables categoricas de la lista
        stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
        encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
        #una vez indexadas utilizamos el OneHotEncoderEstimator que le asigna a cada valor de la variable categórica un número
        stages += [stringIndexer.setHandleInvalid("keep"), encoder]
        #Guardamos este proceso en la variable stages indicandole que si hay valores inválidos los conserve

    label_stringIdx = StringIndexer(inputCol="Burnout_Antes", outputCol="label") #Indexamos como label la variable que queremos predecir que es el Burnout_Antes cuyos valores
                                                                                #Son VERDADERO y FALSO
    stages += [label_stringIdx.setHandleInvalid("keep")]
    # Guardamos este proceso en la variable stages indicandole que si hay valores inválidos los conserve

    numericCols = ['Tiempo_PlazaActual','Hora_Social','Horas_Cuidados','Calorias','Peso','Tiempo_Vida_Laboral','Hijos','Hora_Gratificante','Horas_Activ_Fisica']
    #Con las variables categóricas transformadas a números podemos hacer un vector uniendolo con las variables numéricas.
    assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
    assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
    #este proceso nos da como resultado las "features" que contienen en objeto vector las variables numéricas y categóricas.
    stages += [assembler.setHandleInvalid("keep")]
    # Guardamos este proceso en la variable stages indicandole que si hay valores inválidos los conserve

    from pyspark.ml import Pipeline
    pipeline = Pipeline(stages = stages)
    #Inicializamos nuestro Pipeline y le pasamos la lista de pasos que debe ejecutar, que se encuentran en la variable stages.
    pipelineModel = pipeline.fit(data)
    data = pipelineModel.transform(data)
    #Ejecutamos y entreamos el modelo que sería el procesamiento de los datos.
    path = 'modelo_Pipeline'
    os.mkdir(path)
    pipelineModel.save(os.path.join(path, 'Pipeline'))
    #Guardamos este modelo, debido a que para predecir necesitamos aplicar este mismo modelo a los nuevos datos
    selectedCols = ['label', 'features'] + cols
    data = data.select(selectedCols)
    #Seleccionamos la variable label y features, más la variable cols que contiene las columnas antes de hacer el procesado de datos

    train, test = data.randomSplit([0.7, 0.3])
    #Para el entrenamiento y las pruebas utilizamos entonces un randomSplit para dividir el dataset en un porcentaje 70% entrenamiento y 30% pruebas
    print("Training Dataset Count: " + str(train.count()))
    print("Test Dataset Count: " + str(test.count()))
    #imprimimos la cantidad de filas que tiene cada uno y devolvemos estos datos para su utilización por los algoritmos.
    return train,test

def LogisticRegression(train,test):
    from pyspark.ml.classification import LogisticRegression #importamos la libreria necesaria
    lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=100,elasticNetParam=0.5,fitIntercept=False,threshold=0.8) #establecemos parametros para el entrenamiento
    lrModel = lr.fit(train) #entrenamos
    predictions = lrModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10) #mostramos algunas predicciones
    from pyspark.ml.evaluation import BinaryClassificationEvaluator #improtamos el evaluador binario para evaluar nuestor modelo
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions)) #evaluamos e imprimimos el valor ROC

    from pyspark.ml.tuning import ParamGridBuilder, CrossValidator  #importamos el CrossValidation
    paramGrid = (ParamGridBuilder()
                 .addGrid(lr.maxIter, [100, 500, 1000, 5000, 7000, 10000]) #seleccionamos otro conjunto de caracteristicas
                 .addGrid(lr.elasticNetParam, [0,0.2,0.3,0.4,0.5,0.7,0.8])
                 .addGrid(lr.fitIntercept, [True, False])
                 .addGrid(lr.threshold, [1,0.9,0.8])
                 .build())
    cv = CrossValidator(estimator=lr, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=10) #ejecutamos el crossvalidator donde se van a entrenar varios modelos
    cvModel = cv.fit(train)                                                                         # de logistic Regression y el se quedara con el que mejor probabilidades tenga
    path = 'modelo_LogisticRegression'      #guardamos el modelo
    os.mkdir(path)
    cvModel.save(os.path.join(path, 'modelLogisticRegression'))
    predictions = cvModel.transform(test)
    print('Test Area Under ROC', evaluator.evaluate(predictions)) #probamos nuevamente el ROC

def RandomForest(train,test):
    from pyspark.ml.classification import RandomForestClassifier #importamos la libreria necesaria
    rf = RandomForestClassifier(featuresCol='features', labelCol='label',numTrees=500,featureSubsetStrategy="all") #establecemos los parametros para el entrenamiento
    rfModel = rf.fit(train) #entrenamos
    predictions = rfModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10) #mostramos algunas predicciones

    from pyspark.ml.evaluation import BinaryClassificationEvaluator #improtamos el evaluador binario para evaluar nuestor modelo
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions))
    from pyspark.ml.tuning import ParamGridBuilder, CrossValidator #importamos el Crossvalidator
    paramGrid = (ParamGridBuilder()
                 .addGrid(rf.numTrees, [1000,2500,6000,10000]) #seleccionamos otro conjunto de caracteristicas
                 .addGrid(rf.featureSubsetStrategy, ["all","auto", "sqrt","log2"])
                 .build())
    cv = CrossValidator(estimator=rf, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=2) #jecutamos el crossvalidation donde se van a entrenar varios modelos
                                                                                                #de random forest y el se quedara con el que mejor probabilidades tenga
    cvModel = cv.fit(train)
    path = 'modelo_RandomForest'  #guardamos el modelo
    os.mkdir(path)
    cvModel.save(os.path.join(path, 'modelRandomForest'))
    predictions = cvModel.transform(test)
    print('Test Area Under ROC', evaluator.evaluate(predictions)) #probamos nuevamente el ROC

def DecisionTree(train,test):
    from pyspark.ml.classification import DecisionTreeClassifier #importamos la libreria necesaria
    modelTree = DecisionTreeClassifier(featuresCol='features', labelCol='label',maxDepth=30,minInfoGain=0.4,maxBins=18) #establecemos los parametros para el entrenamiento
    TreeModel = modelTree.fit(train)#entrenamos
    predictions = TreeModel.transform(test)
    predictions.select('Burnout_Antes', 'label', 'rawPrediction', 'prediction', 'probability').show(10) #mostramos algunas predicciones
    from pyspark.ml.evaluation import BinaryClassificationEvaluator#improtamos el evaluador binario para evaluar nuestor modelo
    evaluator = BinaryClassificationEvaluator()
    print('Test Area Under ROC', evaluator.evaluate(predictions))

    from pyspark.ml.tuning import ParamGridBuilder, CrossValidator #importamos el crossvalidator
    paramGrid = (ParamGridBuilder()
                 .addGrid(modelTree.maxDepth, [5, 15, 30]) #seleccionamos otro conjunto de caracteristicas
                 .addGrid(modelTree.minInfoGain, [0,0.4,0.8])
                 .addGrid(modelTree.maxBins, [18, 20,10,5,2])
                 .build())
    cv = CrossValidator(estimator=modelTree, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=10)#jecutamos el crossvalidation donde se van a entrenar varios modelos
                                                                                                #de random forest y el se quedara con el que mejor probabilidades tenga
    cvModel = cv.fit(train)
    path = 'modelo_DecisionTree' #guardamos el modelo
    os.mkdir(path)
    cvModel.save(os.path.join(path, 'modelDecisionTree'))
    predictions = cvModel.transform(test)
    print('Test Area Under ROC', evaluator.evaluate(predictions)) #probamos nuevamente el ROC




train,test = DataPreparation()
#LogisticRegression(train,test)
#RandomForest(train,test)
#DecisionTree(train,test)








