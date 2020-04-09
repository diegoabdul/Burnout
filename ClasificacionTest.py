import matplotlib.pyplot as plt
import numpy as np
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.classification import DecisionTreeClassificationModel
from pyspark.ml.tuning import CrossValidatorModel
from pyspark.ml.regression import IsotonicRegressionModel
import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

def DataPreparation():
    spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
    data = spark.read.csv("test.csv",header=True, inferSchema=True)
    #data = spark.createDataFrame(df)
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
    lrModel = CrossValidatorModel.load(path)
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
    randomModel = CrossValidatorModel.load(path)
    predictions = randomModel.transform(data)
    prediccion = predictions.select('prediction', 'probability').rdd.flatMap(lambda x: x).collect()
    if prediccion[0] == 1.0:
        prediccionLabel = 'FALSO'
    else:
        prediccionLabel = 'VERDADERO'

    return prediccionLabel, prediccion[1][0] * 100

def DecisionTree(data):
    path = 'modelo_DecisionTree/modelDecisionTree'
    DecisionTree = CrossValidatorModel.load(path)
    predictions = DecisionTree.transform(data)
    prediccion = predictions.select('prediction', 'probability').rdd.flatMap(lambda x: x).collect()
    print(prediccion[0])
    if prediccion[0] == 1.0:
        prediccionLabel = 'FALSO'
    else:
        prediccionLabel = 'VERDADERO'

    return prediccionLabel, prediccion[1][0] * 100






data=DataPreparation()

prediccionLinear,probabilidadLineal=LinearEvaluation(data)
# prediccionRandom,probabilidadForest=RandomForest(data)
prediccionTree,probabilidadTree=DecisionTree(data)
print(prediccionLinear + ' ' + str(probabilidadLineal) + ' Logistic Regresion')
# print(prediccionRandom + ' ' + str(probabilidadForest) + ' Random Forest ')
print(prediccionTree + ' ' + str(probabilidadTree) + ' DecisionTree ')


