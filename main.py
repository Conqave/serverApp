import mysql.connector
import socket
import time
import requests
import codecs
import datetime

def getHttp(a):
    r = requests.get(a)

    ans = codecs.decode(r.content, 'UTF-8')
    return ans

def getTimestamp():
    ct = datetime.datetime.now()
    return ct.time()

def getName(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!4")
    c = a.find("!5")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getIsInDanger(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!5")
    c = a.find("!6")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getLocalisation(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!6")
    c = a.find("!7")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getBatteryVoltage(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!7")
    c = a.find("!8")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getPulseOximeter(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!8")
    c = a.find("!9")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getSweat(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!9")
    c = a.find("!10")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getPh(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!10")
    c = a.find("!11")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getSMS(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!11")
    c = a.find("!12")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def getLocalisationX(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!13")
    c = a.find("!14")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp


def getLocalisationY(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!14")
    c = a.find("!15")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp


def getLocalisationZ(a): #Zmienna a jest pobierana przez funkcję getHttp, a więc będzie a = getHttp(tutaj adres)
    b = a.find("!15")
    c = a.find("!16")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp


#print(getTimestamp())

def putRecordIntoDatabase(a):
    name = getName(a)
    isInDanger = getIsInDanger(a)
    localisation = getLocalisation(a)
    batteryVoltage = getBatteryVoltage(a)
    pulseOximeter = getPulseOximeter(a)
    sweat = getSweat(a)
    pH = getPh(a)
    sms = getSMS(a)
    timestamp = getTimestamp()
    localisationX = getLocalisationX(a)
    localisationY = getLocalisationY(a)
    localisationZ = getLocalisationZ(a)

    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO main1 (id, name, isInDanger, localisation, batteryVoltage, pulseOximeter, sweat, pH, sms, timestamp, localisationX, localisationY, localisationZ) VALUES (0, "+id+", "+name+", "+isInDanger+", "+localisation+", "+batteryVoltage+", "+pulseOximeter+", "+sweat+", "+pH+", "+sms+", "+timestamp+", "+localisationX+", "+localisationY+", "+localisationZ+")"
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    

putRecordIntoDatabase(getHttp("192.168.1.177"))
#print(getHttp("http://192.168.1.177"))

#sequence = input("Type code to decode: ")
sequence = "!1eband!21!3"
def selectText(a, b, c):
    temp = ""
    
    for x in range(b, c):
        temp+=a[x]
    return temp

#print(selectText("ala ma kota", 0, 4))

def getPuls(d):
    a = getHttp(d)
    b = a.find("!4")
    c = a.find("!5")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp


def countExclamationMarks(a):
    return a.count("!")
    
def checkID(a):
    b = a.find("!2")
    c = a.find("!3")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
    return temp

def hello(a):
    b = a.find("!1")
    c = a.find("!2")
    temp = ""
    
    for x in range(b+2, c):
        temp += a[x]
   
    return temp=="eband"

print(checkID(sequence))

#if hello(sequence):
    

listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname()

listensocket.bind(('', Port))

listensocket.listen(maxConnections)
print("Server has been started at " + IP + " on port " + str(Port))


running = True


#while True:
#    print(getPuls("http://192.168.1.177"))


while running:
    clientsocket, address = listensocket.accept()
    print("New connection has been made!")
    
    
    message = clientsocket.recv(1024).decode()
    ans = "Witam!"
    

    #tutaj jest kod do połączenia z androidem
    #host2="tutaj wpisz hosta"
    #port=tutaj podaj port
    #s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #s.connect((host, port))
    #st='Connection done!'
    #byt = ans.encode()
    #s.send(byt)


    #print("Cos tam")
    if message != "":
        print(message)
    if hello(message):
        print("Welecome!")
            
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
