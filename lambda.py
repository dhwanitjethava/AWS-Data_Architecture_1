import json
import boto3
import pymysql
import pymysql.cursors

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TO DO implement

    #1 - Print S3 bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(bucket)

    #2 - Print .json filename
    json_file = event['Records'][0]['s3']['object']['key']
    print(json_file)

    #3 - Print file objects(metadata) of json_file
    json_file_obj = s3_client.get_object(Bucket=bucket, Key=json_file)
    print(json_file_obj)

    #4 - Print the file content
    data = json_file_obj['Body'].read().decode('utf-8')
    print(data)

    #5 - RDS Database details
    db_host  = "employee-db.ckjx6d5wnbya.ap-south-1.rds.amazonaws.com"
    db_username = "admin" 
    db_password = "admin1234" 
    db_name = "sys" 
    connection = None
    
    #6 - Connect to RDS database instance
    try:
        connection = pymysql.connect(host = db_host, user = db_username, password = db_password, database = db_name, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as e:
        print("ERROR: Could not connect to MySQL instance.")

    #7 - Create table in RDS Database (condition: if table not exist)
    try:
        cur = connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS sys.employees (userId INT NOT NULL, firstName VARCHAR(45) NOT NULL, lastName VARCHAR(45) NOT NULL, jobTitleName VARCHAR(45) NOT NULL, phoneNumber VARCHAR(45) NOT NULL, PRIMARY KEY (userId))")
        connection.commit()
    except:
        print("ERROR: Could not create table in MySQL instance.")

    #8 - Fatch data from S3 bucket and dump into RDS database   
    with connection.cursor() as cur:
        # Iterate over S3 json file content and insert into MySQL database
        for emp in data: 
            try:
                # emp = emp.split(",")
                # print (">>>"+emp)
                empData = data[emp]
                print(empData)
                cur.execute('INSERT INTO sys.employees (userId,firstName,lastName,jobTitleName,phoneNumber) \
                values("'+empData["userId"]+'","'+empData["firstName"]+'","'+empData["lastName"]+'","'+empData["jobTitleName"]+'","'+empData["phoneNumber"]+'",)')
                connection.commit()
            except:
                continue
        cur.execute("SELECT COUNT(*) FROM sys.employees")
    
    #9 - Delete After dumping data in RDS
    print("Deleting the json file from S3 bucket")
    try:
        response = s3_client.delete_object(Bucket=bucket, Key=json_file)
    except Exception as e:
        print(e)
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }