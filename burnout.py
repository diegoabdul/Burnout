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

# Create credentials with Drive & BigQuery API scopes
# Both APIs must be enabled for your project before running this code
project='burnout-258011'
credentials,project = google.auth.default(scopes=['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/bigquery',])

def insertUsuarios():
    # Abrimos el archivo CSV
    f = open('C:/Users/diego/Desktop/Diego/burnout data/usuariosDiego.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    #row[21]  #CANSANCIO EMOCIONAL NIVEL BURNOUT MAS DE 26
    #row[23] #DESPERSONALIZACION NIVEL BURNOUT MAS DE 9
    #row[25] #REALIZACION PERSONAL NIVEL BURNOUT MENOS DE 34
    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS usuarios (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID), Nombre text, labelBurnout text,Altura int, tiempoDeResidente int,edad int, ejercicioFisico text, email text, especialidad text, estadoCivil text, estudias text, numeroHijos int, ValueID text, lectura text, musica text, password text, peso int, social text, sexo text, tiempoPlazaActual int, tiempoVidaLaboral int, tipoContrato text, tipoTrabajo text, ValorEncuesta int, ultimaEncuesta text, ultimaEncuestaValor int, ultimaEncuestaComentario text, encuestaRp int, viajas text, horasActCuidados int, horasActFisica int, horasActGratificante int, horasActSocial int, contratoAdjunto text )')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO usuarios (Nombre,labelBurnout, Altura , tiempoDeResidente ,edad , ejercicioFisico , email , especialidad , estadoCivil , estudias , numeroHijos , ValueID , lectura , musica , password , peso , social , sexo , tiempoPlazaActual , tiempoVidaLaboral , tipoContrato , tipoTrabajo , ValorEncuesta , ultimaEncuesta , ultimaEncuestaValor , ultimaEncuestaComentario , encuestaRp , viajas , horasActCuidados , horasActFisica , horasActGratificante , horasActSocial , contratoAdjunto  ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if ((float(row[21])>=26) and  (float(row[23])>=9) and (float(row[25])<=34)):
            val = (str(row[0]), "VERDADERO",str(row[1]),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31])
        else:
            val = (
            str(row[0]), "FALSO",str(row[1]), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
            row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
            row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def insertEncuestas():
    # Abrimos el archivo CSV
    f = open('C:/Users/diego/Desktop/Diego/burnout data/encuestasDiego.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS encuestas (ID INT NULL,Nombre text, encuestasAe int, valueEncuesta int,comentarioEncuesta text, valueEncuestaRP int, valueID text, creado text)')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO encuestas (Nombre, encuestasAe , valueEncuesta ,comentarioEncuesta , valueEncuestaRP , ValueID , creado ) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        val = (str(row[0]), str(row[1]),row[2],row[3],row[4],row[6],row[7])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def insertDataDia():

    # Abrimos el archivo CSV
    f = open('C:/Users/diego/Desktop/Diego/burnout data/dataDia.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS dataDia (ID INT NULL,EficienciaSueno INT NULL,ejercicio text NULL,estadoCivil text NULL,estudias text NULL,lectura text NULL,musica text NULL,social text NULL, sexo text NULL,labelBurnout text NULL,Nombre text, creado text, email text,fechaActCorazon text, caloriasOutHeartZone int, maxHeartZone int, minHeartZone int,minutosHeartZone int, nameHeartZone text, restingHeartRate int, intradayTime text, datasetValue int, datasetInterval int, datasetType text)')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO dataDia (Nombre, creado , email ,fechaActCorazon , caloriasOutHeartZone , maxHeartZone , minHeartZone,minutosHeartZone, nameHeartZone,restingHeartRate,intradayTime,datasetValue,datasetInterval,datasetType ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def insertDataSleep():
    # Abrimos el archivo CSV
    f = open('C:/Users/diego/Desktop/Diego/burnout data/dataNoche.csv', 'r',encoding='UTF-8')
    # Omitimos la linea de encabezado
    next(f, None)
    reader = csv.reader(f, delimiter=',')
    contador =0

    # Creamos la tabla si no existe
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS dataNoche (ID INT NULL,Name text,created_at text,email text,sleep_dateOfSleep text,sleep_duration int,sleep_efficiency int,sleep_endTime text,sleep_infoCode int,sleep_levels_data_dateTime text,sleep_levels_data_level text,sleep_levels_data_seconds int,sleep_levels_shortData_dateTime text,sleep_levels_shortData_level text,sleep_levels_shortData_seconds int,sleep_levels_summary_deep_count int,sleep_levels_summary_deep_minutes int,sleep_levels_summary_deep_thirtyDayAvgMinutes int,sleep_levels_summary_light_count int,sleep_levels_summary_light_minutes int,sleep_levels_summary_light_thirtyDayAvgMinutes int,sleep_levels_summary_rem_count int,sleep_levels_summary_rem_minutes int,sleep_levels_summary_rem_thirtyDayAvgMinutes int,sleep_levels_summary_wake_count int,sleep_levels_summary_wake_minutes int,sleep_levels_summary_wake_thirtyDayAvgMinutes int,sleep_logId text,sleep_minutesAfterWakeup int,sleep_minutesAsleep int,sleep_minutesAwake int,sleep_minutesToFallAsleep int,sleep_startTime text,sleep_timeInBed int,sleep_type text)')

    # Llenamos la BD con los datos del CSV
    for row in reader:
        sql = "INSERT INTO dataNoche (Name,created_at,email,sleep_dateOfSleep,sleep_duration,sleep_efficiency,sleep_endTime,sleep_infoCode,sleep_levels_data_dateTime,sleep_levels_data_level,sleep_levels_data_seconds,sleep_levels_shortData_dateTime,sleep_levels_shortData_level,sleep_levels_shortData_seconds,sleep_levels_summary_deep_count,sleep_levels_summary_deep_minutes,sleep_levels_summary_deep_thirtyDayAvgMinutes,sleep_levels_summary_light_count,sleep_levels_summary_light_minutes,sleep_levels_summary_light_thirtyDayAvgMinutes,sleep_levels_summary_rem_count,sleep_levels_summary_rem_minutes,sleep_levels_summary_rem_thirtyDayAvgMinutes,sleep_levels_summary_wake_count,sleep_levels_summary_wake_minutes,sleep_levels_summary_wake_thirtyDayAvgMinutes,sleep_logId,sleep_minutesAfterWakeup,sleep_minutesAsleep,sleep_minutesAwake,sleep_minutesToFallAsleep,sleep_startTime,sleep_timeInBed,sleep_type) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33])
        mycursor.execute(sql, val)
        mydb.commit()
    # Cerramos el archivo y la conexion a la bd
    f.close()
    mydb.commit()
    mycursor.close()

def updateLabelDataDia():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT labelBurnout,ejercicioFisico,estadoCivil,estudias,lectura,musica,social,sexo, ID FROM usuarios ")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        labelBurnout = x[0]
        ejercicio = x[1]
        estadoCivil = x[2]
        estudias = x[3]
        lectura = x[4]
        musica = x[5]
        social = x[6]
        sexo = x[7]
        ID = x[8]
        val = (str(labelBurnout), str(ejercicio),str(estadoCivil),str(estudias),str(lectura),str(musica),str(social),str(sexo),str(ID))
        mycursor = mydb.cursor()
        sql = "UPDATE datadia SET labelBurnout = %s,ejercicio = %s,estadoCivil = %s,estudias = %s,lectura = %s,musica = %s,social = %s,sexo = %s WHERE ID = %s"
        mycursor.execute(sql, val)
        mydb.commit()

def updateIDDia():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID, email FROM usuarios ")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        labelBurnout = x[0]
        email = x[1]
        val = (str(labelBurnout), str(email))
        mycursor = mydb.cursor()
        sql = "UPDATE datadia SET ID = %s WHERE email = %s"
        mycursor.execute(sql, val)
        mydb.commit()

def updateIDNoche():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID, email FROM usuarios ")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        labelBurnout = x[0]
        email = x[1]
        val = (str(labelBurnout), str(email))
        mycursor = mydb.cursor()
        sql = "UPDATE datanoche SET ID = %s WHERE email = %s"
        mycursor.execute(sql, val)
        mydb.commit()

def merge():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dormido")
    myresult = mycursor.fetchall()
    mycursor.close()
    for x in myresult:
        sleep_efficiency = x[0]
        ID = x[1]
        val = (str(sleep_efficiency), str(ID))
        mycursor = mydb.cursor()
        sql = "UPDATE datadia SET EficienciaSueno = %s WHERE ID = %s"
        mycursor.execute(sql, val)
        mydb.commit()

def bigquery_2():
    client = bigquery.Client(credentials=credentials, project=project)
    # Perform a query.
    #QUERY = ('SELECT * FROM ML.EVALUATE(MODEL `burnout-258011.burnout.model`, (SELECT * FROM `burnout-258011.burnout.data`))')
    #QUERY = ('SELECT * FROM `burnout-258011.burnout.data` LIMIT 2')
    #QUERY = ('CREATE MODEL IF NOT EXISTS `burnout-258011.burnout.PRUEBA` OPTIONS ( model_type=\'logistic_reg\', ls_init_learn_rate=.15,l1_reg=1,max_iterations=20,input_label_cols=[\'labelBurnout\'],data_split_method=\'seq\',data_split_eval_fraction=0.3,data_split_col=\'email\') AS SELECT labelBurnout,email,caloriasOutHeartZone,maxHeartZone,minHeartZone,minutosHeartZone,nameHeartZone,restingHeartRate,intradayTime,datasetValue,datasetInterval,datasetType FROM `burnout-258011.burnout.data` ')
    QUERY = ('SELECT * FROM  ML.PREDICT(MODEL `burnout-258011.burnout.PRUEBA`, (SELECT "diegoabdul@hotmail.com" as email,\'2018-05-20\' as fechaActCorazon,2000 as caloriasOutHeartZone,140 as maxHeartZone,120 as minHeartZone,1234 as minutosHeartZone,"Cardio" as nameHeartZone,50 as restingHeartRate,"" as intradayTime,60 as datasetValue,1 as datasetInterval,"minute" as datasetType))')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    for row in rows:
        print(row[0])
        print(row[1][0])
        print(row[1][1])

def SQLtoCSV():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT  * from datadia")
    myresult = mycursor.fetchall()
    mycursor.close()
    with open("burnout.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['ID','EficienciaSueno','ejercicioFisico','estadoCivil','estudias','lectura','musica','social','sexo','labelBurnout','Nombre','creado','email','fechaActCorazon','caloriasOutHeartZone','maxHeartZone','minHeartZone','minutosHeartZone','nameHeartZone','restingHeartRate','intradayTime','datasetValue','datasetInterval','datasetType'])
        csv_writer.writerows(myresult)

def gcs_upload_blob():
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('burnout')
    blob = bucket.blob('burnout.csv')

    blob.upload_from_filename('burnout.csv')

    print('File {} uploaded to {}.'.format('burnout.csv','gs://burnout/burnout.csv'))


def bq_load_csv_in_gcs():
    bigquery_client = bigquery.Client(credentials=credentials, project=project)
    dataset_ref = bigquery_client.dataset('burnout')

    schema = [
        bigquery.SchemaField('ID', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('labelBurnout', 'string', mode='NULLABLE'),
        bigquery.SchemaField('Nombre', 'string', mode='NULLABLE'),
        bigquery.SchemaField('creado', 'TIMESTAMP', mode='NULLABLE'),
        bigquery.SchemaField('email', 'string', mode='NULLABLE'),
        bigquery.SchemaField('fechaActCorazon', 'TIMESTAMP', mode='NULLABLE'),
        bigquery.SchemaField('caloriasOutHeartZone', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('maxHeartZone', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('minHeartZone', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('minutosHeartZone', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('nameHeartZone', 'string', mode='NULLABLE'),
        bigquery.SchemaField('restingHeartRate', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('intradayTime', 'string', mode='NULLABLE'),
        bigquery.SchemaField('datasetValue', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('datasetInterval', 'integer', mode='NULLABLE'),
        bigquery.SchemaField('datasetType', 'string', mode='NULLABLE'),
        bigquery.SchemaField('EficienciaSueno', 'string', mode='NULLABLE'),
        bigquery.SchemaField('ejercicioFisico', 'string', mode='NULLABLE'),
        bigquery.SchemaField('estadoCivil', 'string', mode='NULLABLE'),
        bigquery.SchemaField('estudias', 'string', mode='NULLABLE'),
        bigquery.SchemaField('lectura', 'string', mode='NULLABLE'),
        bigquery.SchemaField('musica', 'string', mode='NULLABLE'),
        bigquery.SchemaField('social', 'string', mode='NULLABLE'),
        bigquery.SchemaField('sexo', 'string', mode='NULLABLE')
    ]
    job_config = bigquery.LoadJobConfig()
    job_config.schema = schema
    job_config.skip_leading_rows = 1

    load_job = bigquery_client.load_table_from_uri(
        'gs://burnout/burnout.csv',
        dataset_ref.table('burnout'),
        job_config=job_config)

    assert load_job.job_type == 'load'

    load_job.result()  # Waits for table load to complete.

    assert load_job.state == 'DONE'

def load_csv_autoMLTables():
    dataset_display_name = 'data'
    path = 'gs://burnout/data.csv'
    client = automl.TablesClient(project=project)
    dataset = client.create_dataset(dataset_display_name)

    response = None
    if path.startswith('bq'):
        response = client.import_data(
            dataset_display_name=dataset_display_name, bigquery_input_uri=path
        )
    else:
        # Get the multiple Google Cloud Storage URIs.
        input_uris = path.split(",")
        response = client.import_data(
            dataset_display_name=dataset_display_name,
            gcs_input_uris=input_uris
        )

    print("Processing import...")
    # synchronous check of operation status.
    print("Data imported. {}".format(response.result()))

def test_autoMLTables():
    # TODO(developer): Uncomment and set the following variables
    model_display_name = 'burnout_final'
    gcs_input_uris = 'gs://burnout/pruebaburnout.csv'
    gcs_output_uri = 'gs://burnout'

    #from google.cloud import automl_v1beta1 as automl

    client = automl.TablesClient(project=project)

    # Query model
    response = client.batch_predict(gcs_input_uris=gcs_input_uris,
                                    gcs_output_uri_prefix=gcs_output_uri,
                                    model_display_name=model_display_name)
    print("Making batch prediction... ")
    response.result()
    print("Batch prediction complete.\n{}".format(response.metadata))



#insertUsuarios()
#insertDataDia()
#insertDataSleep()
#updateIDDia()
#updateLabelDataDia()
#updateIDNoche()
#merge()
#SQLtoCSV()
#gcs_upload_blob()
#bq_load_csv_in_gcs()
test_autoMLTables()