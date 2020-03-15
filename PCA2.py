# Imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

sc =SparkContext()
sqlContext = SQLContext(sc)

spark = SparkSession.builder.master("local[*]").getOrCreate()
data2 = spark.read.csv('Burnout_Data.csv', header = True, inferSchema = True)
data=data2.toPandas()
#data = pd.read_csv('Burnout_Data.csv',low_memory=False)# Standardize the data to have a mean of ~0 and a variance of 1
# Import label encoder
from sklearn import preprocessing
# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()
# Encode labels in column 'Country'.
data['Edad']= label_encoder.fit_transform(data['Edad'])
data['Ejercicio_Fisico']= label_encoder.fit_transform(data['Ejercicio_Fisico'])
data['Especialidad']= label_encoder.fit_transform(data['Especialidad'])
data['EstadoCivil']= label_encoder.fit_transform(data['EstadoCivil'])
data['Estudias']= label_encoder.fit_transform(data['Estudias'])
data['Lectura']= label_encoder.fit_transform(data['Lectura'])
data['Musica']= label_encoder.fit_transform(data['Musica'])
data['Sales_Social']= label_encoder.fit_transform(data['Sales_Social'])
data['Sexo']= label_encoder.fit_transform(data['Sexo'])
data['Tipo_Contrato']= label_encoder.fit_transform(data['Tipo_Contrato'])
data['Tipo_Trabajo']= label_encoder.fit_transform(data['Tipo_Trabajo'])
data['Contrato_Adjunto']= label_encoder.fit_transform(data['Contrato_Adjunto'])
data['Burnout_Antes']= label_encoder.fit_transform(data['Burnout_Antes'])
data['Burnout_Despues']= label_encoder.fit_transform(data['Burnout_Despues'])
data['Niveles_deSueno']= label_encoder.fit_transform(data['Niveles_deSueno'])
data['Email']= label_encoder.fit_transform(data['Email'])
data['Password']= label_encoder.fit_transform(data['Password'])
data['Comentarios2']= label_encoder.fit_transform(data['Comentarios2'])
data['Comentarios']= label_encoder.fit_transform(data['Comentarios'])
data['Estado_Animo']= label_encoder.fit_transform(data['Estado_Animo'])
print(data.head())
X_std = StandardScaler().fit_transform(data)# Create a PCA instance: pca
pca = PCA(n_components=20)
principalComponents = pca.fit_transform(X_std)# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_ratio_, color='black')
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)# Save components to a DataFrame
PCA_components = pd.DataFrame(principalComponents)