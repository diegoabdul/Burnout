import mysql.connector
import csv
import codecs
from google.cloud import bigquery
from google.cloud import storage
import google.auth
from google.cloud import automl_v1beta1 as automl
import matplotlib.pyplot as plot

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
    database="burnout"
)

def insertDataDia():

    # Abrimos el archivo CSV
    f = open('Despierto.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS Despierto (Identificador INT NULL,Email text NULL,Calorias text NULL,Max_HeartRate text NULL,Min_HeartRate text NULL,Tipo_Actividad text NULL,Resting_HeartRate text NULL,Frecuencia_Cardiaca_Minuto text NULL,Sleep_Duration text NULL,Sleep_Efficiency text NULL,Data_Level text NULL,Data_Seconds text NULL,Summary_Deep_Count text NULL,Summary_Deep_Minutes text NULL,Summary_Light_Minutes text NULL,Summary_Rem_Minutes text NULL,Summary_Wake_Minutes text NULL,MinutesAsleep text NULL,MinutesAwake text NULL,minutesToFallAsleep text NULL,timeInBed text NULL)')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO Despierto (Identificador,Email,Calorias,Max_HeartRate,Min_HeartRate,Tipo_Actividad,Resting_HeartRate,Frecuencia_Cardiaca_Minuto ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def insertDataNoche():

    # Abrimos el archivo CSV
    f = open('Dormido.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS Dormido (Identificador INT NULL,Email text NULL,Sleep_Duration text NULL,Sleep_Efficiency text NULL,Data_Level text NULL,Data_Seconds text NULL,Summary_Deep_Count text NULL,Summary_Deep_Minutes text NULL,Summary_Light_Minutes text NULL,Summary_Rem_Minutes text NULL,Summary_Wake_Minutes text NULL,MinutesAsleep text NULL,MinutesAwake text NULL,minutesToFallAsleep text NULL,timeInBed text NULL)')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO Dormido (Identificador,Email ,Sleep_Duration ,Sleep_Efficiency ,Data_Level ,Data_Seconds ,Summary_Deep_Count ,Summary_Deep_Minutes ,Summary_Light_Minutes ,Summary_Rem_Minutes ,Summary_Wake_Minutes ,MinutesAsleep ,MinutesAwake,minutesToFallAsleep ,timeInBed ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def merge():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Identificador,Sleep_Duration ,Sleep_Efficiency ,Data_Level ,Data_Seconds ,Summary_Deep_Count ,Summary_Deep_Minutes ,Summary_Light_Minutes ,Summary_Rem_Minutes ,Summary_Wake_Minutes ,MinutesAsleep ,MinutesAwake,minutesToFallAsleep ,timeInBed  FROM dormido")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        ID = x[0]
        a = x[1]

        val = (str(sleep_efficiency), str(ID))
        mycursor = mydb.cursor()
        sql = "UPDATE datadia SET Sleep_Duration = %s,Sleep_Efficiency = %s,Data_Level = %s,Data_Seconds = %s,Summary_Deep_Count = %s,Summary_Deep_Minutes = %s,Summary_Light_Minutes = %s,Summary_Rem_Minutes = %s,Summary_Wake_Minutes = %s,MinutesAsleep = %s,MinutesAwake= %s,minutesToFallAsleep = %s,timeInBed = %s WHERE ID = %s"
        mycursor.execute(sql, val)
        mydb.commit()

insertDataDia()
