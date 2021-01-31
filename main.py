import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='s8.zenbox.pl',
                                         database='agd1001_eband',
                                         user='agd1001_eucys',
                                         password='12345678')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM main1")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")