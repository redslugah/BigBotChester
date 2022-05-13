import mysql.connector
from mysql.connector import Error
import pandas as pd

def createServerConnection(hostName, userName, userPassword):
    connection = None
    try:
        connection = mysql.connector.connect(host = hostName, user = userName, passwd = userPassword)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def createDatabase(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
def createDbConnection(hostName, userName, userPassword, dbName):
    connection = None
    try:
        connection = mysql.connector.connect(host = hostName, user = userName, passwd = userPassword, database = dbName)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful:\n"+query)
    except Error as err:
        print(f"Error: '{err}'")
        
def readQuery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query successful: \n"+query)
        return result
    except Error as err:
        print(f"Error: '{err}'")