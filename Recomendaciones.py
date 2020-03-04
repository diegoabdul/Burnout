#Hacemos las importaciones necesarias
import time
from pyspark.sql import SparkSession
#Inicializamos la variable tiempo para medir el tiempo de ejecucion total
start_time = time.time()
from pyspark.ml.recommendation import ALS
#Creamos una nueva sesión Spark
spark = SparkSession.builder.master("local[*]").getOrCreate()
#Leemos los csv y los transformamos en un dataframe, con una reparticion de 10, si no le colocamos
#reparticion lo haria automaticamente
dataset_tam = 'ml-latest-small'
movies_df = spark.read.csv('movies.csv'.format(dataset_tam),header=True, inferSchema=True).repartition(10).cache()
movies_df.printSchema()
#vamos mostrando el esquema o las columnas que ha leido de cada csv
ratings_df = spark.read.csv('ratings.csv'.format(dataset_tam),header=True, inferSchema=True).repartition(10).cache()
ratings_df.printSchema()

ratings_df.describe().show()
ratings_df.createOrReplaceTempView('rating')
#aplicamos el modelo ASL
model = ALS(userCol='userId', itemCol='movieId', ratingCol='rating').fit(ratings_df)
#tranformamos el modelo segun el dataframe ratings_df
predicciones = model.transform(ratings_df)
predicciones.toPandas().head()

from pyspark.ml.evaluation import RegressionEvaluator
#hacemos la evaluacion mediante la regresion, esto nos devuelve que tan cercanas son nuestras predicciones
evaluator = RegressionEvaluator(metricName='rmse', labelCol='rating', predictionCol='prediction')
print('The root mean squared error for our model is: {}'.format(evaluator.evaluate(predicciones)))

from pyspark.sql.functions import lit

def recommendMovies(model, user, nbRecommendations):
    #entramos en la funcion que se le debe pasar el modelo, el numero de usuario a recomendar, y el numero de recomendaciones deseadas
    #primero conseguimos el subconjunto de datos para ese usuario en particular
    dataSet = ratings_df.select('movieId').distinct().withColumn('userId', lit(user))
    #conseguimos luego las peliculas que el usuario ha visto y a valorado
    moviesAlreadyRated = ratings_df.filter(ratings_df.userId == user).select('movieId', 'userId')
    #eliminamos estas peliculas porque no tiene sentido recomendarle una pelicula que ya vio
    predictions = model.transform(dataSet.subtract(moviesAlreadyRated)).dropna().orderBy('prediction', ascending=False).limit(nbRecommendations).select('movieId', 'prediction')
    #hacemos las prediccion con el limite establecido en la funcion y lo devolvemos
    recommendations = predictions.join(movies_df, predictions.movieId == movies_df.movieId).select(predictions.movieId, movies_df.title, movies_df.genres, predictions.prediction)
    return recommendations

print('Recommendations for user 8:')
#hacemos la llamada a la funcion con los valores requeridos, el modelo, el numero del usuario y la cantidad de recomendaciones deseadas
#imprimimos el return para ver cuales serian estas peliculas
print(recommendMovies(model, 8, 10).toPandas())
#tomamos el tiempo actual y se lo restamos del tiempo inicial, de esta manera tendriamos el tiempo que ha tardado en ejecutar el programa.
end=time.time()
elapsed_time = end - start_time
print(time.strftime("%H:%M:%S",time.gmtime(elapsed_time)))