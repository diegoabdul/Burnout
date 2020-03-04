import os
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.appName('SistemaDeDeteccion').getOrCreate()
df = spark.read.csv('Burnout_Data.csv', header = True, inferSchema = True)
df.printSchema()
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

label_stringIdx = StringIndexer(inputCol = 'Burnout_Antes', outputCol = 'label')
stages += [label_stringIdx]

numericCols = ['Frecuencia_Cardiaca_Minuto']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler.setHandleInvalid("skip")]

from pyspark.ml import Pipeline
pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
#selectedCols = ['label', 'features'] + cols
#df2 = df.select(selectedCols)
#df2.printSchema()

train, test = df.randomSplit([0.7, 0.3])
print("Training Dataset Count: " + str(train.count()))
print("Test Dataset Count: " + str(test.count()))
test.show()
from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator# Create ParamGrid for Cross Validation
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
evaluator = MulticlassClassificationEvaluator(predictionCol="prediction")
paramGrid = (ParamGridBuilder()
             .addGrid(lr.regParam, [0.1, 0.3, 0.5]) # regularization parameter
             .addGrid(lr.elasticNetParam, [0.0, 0.1, 0.2]) # Elastic Net Parameter (Ridge = 0)
#            .addGrid(model.maxIter, [10, 20, 50]) #Number of iterations
#            .addGrid(idf.numFeatures, [10, 100, 1000]) # Number of features
             .build())# Create 5-fold CrossValidator
cv = CrossValidator(estimator=lr, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)
cvModel = cv.fit(train)
predictions = cvModel.transform(test)
print(evaluator.evaluate(predictions))
#path = 'model_rfc'
#os.mkdir(path)
#lrModel.save(os.path.join(path, 'model_1'))








