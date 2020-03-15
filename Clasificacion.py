import matplotlib.pyplot as plt
import numpy as np
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.classification import RandomForestClassificationModel
import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

def DataPreparation(df):
    spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
    #data = spark.read.csv("test.csv",header=True, inferSchema=True)
    data = spark.createDataFrame(df)
    data = data.select('Tiempo_PlazaActual', 'EstadoCivil', 'Hora_Social', 'Horas_Cuidados',
                       'Resting_HeartRate', 'Calorias', 'Frecuencia_Cardiaca_Minuto', 'Peso', 'Contrato_Adjunto', 'Musica',
                       'Sexo', 'Estudias', 'Sales_Social', 'Edad', 'Estado_Animo', 'Cantidad_Sueno_Profundo',
                       'Tiempo_Vida_Laboral', 'Hijos', 'Lectura', 'Minutos_Dormido')
    data.show()

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
    predictions = lrModel.transform(data)
    predictions.show()

def RandomForest(data):
    path = 'modelo_RandomForest/modelRandomForest'
    randomModel = RandomForestClassificationModel.load(path)
    predictions = randomModel.transform(data)
    predictions.show()


#data=DataPreparation()
#LinearEvaluation(data)
#RandomForest(data)



