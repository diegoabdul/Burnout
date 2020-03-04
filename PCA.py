from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.ml.feature import PCA, VectorAssembler
from pyspark.mllib.linalg import Vectors
from pyspark.ml import Pipeline
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.mllib.feature import Normalizer
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kde

sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
df = spark.read.csv('Burnout_Data.csv', header = True, inferSchema = True)
df = df.select('Burnout_Antes','Ejercicio_Fisico','Frecuencia_Cardiaca_Minuto')
cols = df.columns
# df.printSchema()
#
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
categoricalColumns = ['Ejercicio_Fisico']
stages = []

for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    stages += [stringIndexer, encoder]

#label_stringIdx = StringIndexer(inputCol = 'Burnout_Antes', outputCol = 'label')
#stages += [label_stringIdx]

numericCols = ['Frecuencia_Cardiaca_Minuto']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler.setHandleInvalid("skip")]


pca = PCA(k=2, inputCol="features", outputCol="pcaFeatures")

from pyspark.ml import Pipeline
pipeline = Pipeline(stages = [stages,pca])
print(df.head)
model = pipeline.fit(df)

xy = model.transform(df).select("pcaFeatures").map(lambda row: [row[0][0], row[0][1]]).collect()

xy = np.array(xy)

x=np.array(zip(*xy)[0])
y=np.array(zip(*xy)[1])

#plt.scatter(x,y)
#plt.show()

plt.hexbin(x,y,  gridsize=30)
plt.show()

nbins = 55

k = kde.gaussian_kde(np.transpose(xy))
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
plt.show()


