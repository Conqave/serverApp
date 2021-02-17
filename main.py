import mysql.connector
import socket
import time

listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname()

listensocket.bind(('', Port))

listensocket.listen(maxConnections)
print("Server has been started at " + IP + " on port " + str(Port))


running = True

while running:
    (clientsocket, address) = listensocket.accept()
    print("New connection has been made!")
    
    message = clientsocket.recv(1024).decode()
    #print("Cos tam")
    if message != "":
        print(message)
        
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
