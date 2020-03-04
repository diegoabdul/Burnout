import mysql.connector
import csv
import codecs

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
    database="burnout"
)

def SQLtoCSVData():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT  * from datadia")
    myresult = mycursor.fetchall()
    mycursor.close()
    with open("burnout.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['ID','EficienciaSueno','ejercicioFisico','estadoCivil','estudias','lectura','musica','social','sexo','labelBurnout','Nombre','creado','email','fechaActCorazon','caloriasOutHeartZone','maxHeartZone','minHeartZone','minutosHeartZone','nameHeartZone','restingHeartRate','intradayTime','datasetValue','datasetInterval','datasetType'])
        csv_writer.writerows(myresult)
def SQLtoCSVUsuarios():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from usuarios where ID IN (SELECT distinct ID FROM datadia)")
    myresult = mycursor.fetchall()
    mycursor.close()
    with open("usuarios.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['ID','Nombre','labelBurnout','Altura','tiempoDeResidente','edad','ejercicioFisico','email','especialidad','estadoCivil','estudias','numeroHijos','ValueID','lectura','musica','password','peso','social','sexo','tiempoPlazaActual','tiempoVidaLaboral','tipoContrato','tipoTrabajo','ValorEncuesta','ultimaEncuesta','ultimaEncuestaValor','ultimaEncuestaComentario','encuestaRp','viajas','horasActCuidados','horasActFisica','horasActGratificante','horasActSocial','contratoAdjunto'])
        csv_writer.writerows(myresult)
SQLtoCSVData()