# Input an xlsx file and push the data into mariadb

import pandas as pd
import pymysql
import argparse

parser = argparse.ArgumentParser(description='Push data from Wyscout .xlsx files to MariaDB')

parser.add_argument('-f', '--file', help="REQUIRED -- Provide the path to the .xlsx file to be cleaned", default=None)
parser.add_argument('-p', '--password', help="REQUIRED -- Your MariaDB password. Change your username in the .py file")

args = parser.parse_args()

# Read data from an Excel file
excel_file = args.file  # replace with your file name and path
df = pd.read_excel(excel_file)

# Connect to MariaDB
mariadb_host = '192.168.0.196'  # replace with your MariaDB hostname or IP address
mariadb_user = 'cdoss'  # replace with your MariaDB username
mariadb_password = args.password  # replace with your MariaDB password
mariadb_db = 'btl'  # replace with your MariaDB database name

connection = pymysql.connect(host=mariadb_host, user=mariadb_user, password=mariadb_password, db=mariadb_db)
cursor = connection.cursor()

# Define the SQL query to create a table based on the Excel file structure (columns and data types)
create_table_query = "CREATE TABLE IF NOT EXISTS excel_data ("

for column in df.columns:
    column_type = df[column].dtype
    if column_type == 'object':
        create_table_query += f"{column} VARCHAR(255),"
    elif column_type == 'float64' or column_type == 'int64':
        create_table_query += f"{column} DECIMAL(10,2),"
cursor.execute(create_table_query[:-1] + ");")  # Remove the trailing comma and execute the query

# Insert data into the MariaDB table
for index, row in df.iterrows():
    values = tuple(row)
    insert_query = "INSERT INTO excel_data VALUES (" + ",".join([f"%s" for _ in range(len(values))]) + ");"
    cursor.execute(insert_query, values)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()