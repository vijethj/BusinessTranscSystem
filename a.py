import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="vijeth1728")
c = mydb.cursor()
c.execute("CREATE DATABASE pes1ug20cs499_project")