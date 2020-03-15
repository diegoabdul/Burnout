from boto import sns
from plotly.plotly import plotly
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.master("local[*]").getOrCreate()
data = spark.read.csv('Burnout_Data.csv', header = True, inferSchema = True)
data = data.drop('Email')
data = data.drop('Password')
data = data.drop('Comentarios2')
data = data.drop('Comentarios')
data = data.drop('Estado_Animo')
data = data.drop('Minutos_Sueno_Profundo')
data = data.drop('Minutos_Sueno_Ligero')
data = data.drop('Minutos_Rem')
data = data.drop('Minutos_Sueno_Wake')
data = data.drop('Minutos_Dormido')
data = data.drop('Minutos_Despierto_enCama')
data = data.drop('Minutos_paraDormir')
data = data.drop('Tiempo_enCama')
#data = data.select('Identificador','Frecuencia_Cardiaca_Minuto','Calorias')

from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
categoricalColumns = ['Edad','Ejercicio_Fisico','Especialidad','EstadoCivil','Estudias','Lectura','Musica','Sales_Social','Sexo','Tipo_Contrato','Tipo_Trabajo','Contrato_Adjunto','Burnout_Antes','Burnout_Despues','Niveles_deSueno']
#categoricalColumns= ['Edad','Ejercicio_Fisico']
stages = []

for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    stages += [stringIndexer.setHandleInvalid("keep"), encoder]

#numericCols = ['Frecuencia_Cardiaca_Minuto','Calorias']
numericCols = ['Altura','Anos_Residente','Hijos','Peso','Tiempo_PlazaActual','Tiempo_Vida_Laboral','Ultima_Encuesta_Cansancio_Emocional','Ultima_Encuesta_Despersonalizacion','Ultima_Encuesta_Realizacion_Personal','Viajas','Horas_Cuidados','Horas_Activ_Fisica','Hora_Gratificante','Hora_Social','Cansancio_Emocional','Despersonalizacion','Realizacion_Personal','Calorias','Max_HeartRate','Min_HeartRate','Resting_HeartRate','Frecuencia_Cardiaca_Minuto','Duracion_Sueno','Eficiencia_Sueno']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler.setHandleInvalid("keep")]

from pyspark.ml import Pipeline
pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(data)
data = pipelineModel.transform(data)
# Standardize the data to have a mean of ~0 and a variance of 1

from pyspark.ml.feature import PCA
pca = PCA(k=20, inputCol='features', outputCol='features_pca')
pca_model = pca.fit(data)
pca_data = pca_model.transform(data).select('features_pca')
print(pca_model.explainedVariance)

plt.bar(range(1,len(pca_model.explainedVariance)+1),pca_model.explainedVariance)
plt.ylabel('Explained variance')
plt.xlabel('Components')
plt.plot(range(1,len(pca_model.explainedVariance)+1),
         np.cumsum(pca_model.explainedVariance),
         c='red',
         label="Cumulative Explained Variance")
plt.legend(loc='upper left')

plt.plot(pca_model.explainedVariance)
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')
plt.show()

print(pca_model.components)
print(pca_model.pc)


