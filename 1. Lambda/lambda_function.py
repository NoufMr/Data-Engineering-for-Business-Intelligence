import requests
import os
import snowflake.connector as sf
import toml
from dotenv import load_dotenv

def get_file_from_url():
    # Gets file content from url
    # Input: URL, Destination Folder, File Name
    # Output: File Content
    
    # requests parameters
    url = toml.load('config.toml')['url']['url']
    
    # os parameters
    destination_folder = toml.load('config.toml')['os']['destination_folder']
    file_name = toml.load('config.toml')['os']['file_name']
    
    # access inventory file from url
    response = requests.get(url)
    response.raise_for_status()
    
    # save to /tmp/ folder and print file
    file_path = os.path.join(destination_folder, file_name) 
    
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    print("File obtained successfully from url")

def load_file_to_snowflake():
    # Loads data from the file content to snowflake
    # Input: Snowflake Parameters (dotenv: user, password, account) and 
    # (toml: warehouse, database, schema, role, file format, stage, table)
    # Output: Snowflake file format, stage, put condition, inventory data

    # snowflake parameters
    load_dotenv()
    user = os.getenv('user')
    password = os.getenv('password')
    account = os.getenv('account')
    
    warehouse = toml.load('config.toml')['sf']['warehouse']
    database = toml.load('config.toml')['sf']['database']
    schema = toml.load('config.toml')['sf']['schema']
    role = toml.load('config.toml')['sf']['role']
    file_format_name = toml.load('config.toml')['sf']['file_format_name']
    stage_name = toml.load('config.toml')['sf']['stage_name']
    table = toml.load('config.toml')['sf']['table']
    
    # connect to snowflake
    conn = sf.connect(user=user, password=password, account=account, warehouse=warehouse, database=database, schema=schema, role=role)
    conn.cursor()
    
    # use warehouse
    cursor.execute(f"use warehouse {warehouse}")
    # use schema
    cursor.execute(f"use schema {schema}")
    # create file format
    cursor.execute(f"create or replace file format {file_format_name} type='csv' field_delimiter=',';")
    # create stage
    cursor.execute(f"create or replace stage {stage_name} file_format={file_format_name};")
    # run put condition
    cursor.execute(f"put file://{file_path} @{stage_name};")
    # list stage
    cursor.execute(f"list @{stage_name};")
    # truncate table
    cursor.execute(f"truncate table {schema}.{table};")
    # copy into table
    cursor.execute(f"copy into {schema}.{table} from @{stage_name}/{file_name} file_format={file_format_name} on_error='continue';")
    
    print("File uploaded successfully into snowflake")

def lambda_handler(event, context):
    # get inventory file from url
    get_file_from_url()
    
    # load inventory file to snowflake
    load_file_to_snowflake()
    
    return {
        'statusCode': 200,
        'body': "File obtained from url and uploaded into snowflake successfully"
    }