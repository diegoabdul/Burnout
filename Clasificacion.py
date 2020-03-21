import matplotlib.pyplot as plt
import numpy as np
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.classification import GBTClassificationModel
from pyspark.ml.regression import IsotonicRegressionModel
import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

def DataPreparation(df):
    spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
    #data = spark.read.csv("Burnout_Data.csv",header=True, inferSchema=True)
    #df.to_csv('test.csv', index=False)
    data = spark.createDataFrame(df)
    data = data.select('Tiempo_PlazaActual', 'EstadoCivil', 'Hora_Social', 'Horas_Cuidados',
                       'Calorias', 'Peso', 'Contrato_Adjunto', 'Musica', 'Sexo', 'Estudias', 'Sales_Social', 'Edad',
                       'Estado_Animo', 'Tiempo_Vida_Laboral', 'Hijos', 'Lectura', 'Hora_Gratificante',
                       'Horas_Activ_Fisica')
    cols = data.columns

    from pyspark.ml import PipelineModel
    path = 'modelo_Pipeline/Pipeline'
    pipeline = PipelineModel.load(path)
    data = pipeline.transform(data)
    selectedCols = ['features']
    data = data.select(selectedCols)
    return data

def LinearEvaluation(data):
    path = 'modelo_LogisticRegression/modelLogisticRegression'
    lrModel = LogisticRegressionModel.load(path)
    #print(lrModel.coefficientMatrix)
    #predictions=lrModel.transform(data)
    predictions = lrModel.transform(data) #VERDADERO = 0 Y FALSO 1
    prediccion = predictions.select('prediction', 'probability').rdd.flatMap(lambda x: x).collect()
    if prediccion[0] == 1.0:
        prediccionLabel='FALSO'
    else:
        prediccionLabel='VERDADERO'

    return prediccionLabel,prediccion[1][0]*100

def RandomForest(data):
    path = 'modelo_RandomForest/modelRandomForest'
    randomModel = RandomForestClassificationModel.load(path)
    predictions = randomModel.transform(data)
    prediccion = predictions.select('prediction', 'probability').rdd.flatMap(lambda x: x).collect()
    if prediccion[0] == 1.0:
        prediccionLabel = 'FALSO'
    else:
        prediccionLabel = 'VERDADERO'

    return prediccionLabel, prediccion[1][0] * 100

def GradientTree(data):
    path = 'modelo_GradientBoosted/modelGradientBoosted'
    GradientModel = GBTClassificationModel.load(path)
    predictions = GradientModel.transform(data)
    predictions.select('prediction', 'probability').show()
    prediccion = predictions.select('prediction', 'probability').rdd.flatMap(lambda x: x).collect()
    if prediccion[0] == 1.0:
        prediccionLabel = 'FALSO'
    else:
        prediccionLabel = 'VERDADERO'

    return prediccionLabel, prediccion[1][0] * 100

def Isotonic(data):
    path = 'modelo_IsotonicRegression/modelIsotonicRegression'
    GradientModel = IsotonicRegressionModel.load(path)
    predictions = GradientModel.transform(data)
    predictions.show(truncate=False)
    predictions.select('prediction').show()
    prediccion = predictions.select('prediction').rdd.flatMap(lambda x: x).collect()
    if prediccion[0] > 0.5:
        prediccionLabel = 'FALSO'
    else:
        prediccionLabel = 'VERDADERO'

    return prediccion[0],prediccionLabel


#data=DataPreparation()
#LinearEvaluation(data)
#RandomForest(data)



