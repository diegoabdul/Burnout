import matplotlib.pyplot as plt
import numpy as np
from pyspark.ml.classification import LogisticRegressionModel
import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()

path = 'model_rfc/model_1'
lrModel = LogisticRegressionModel.load(path)
beta = np.sort(lrModel.coefficients)
plt.plot(beta)
plt.ylabel('Beta Coefficients')
plt.show()
