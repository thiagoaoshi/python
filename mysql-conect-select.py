import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456",
  database="thiago",
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM tb_dados")
sql = "SELECT * FROM tb_dados ORDER BY endereco"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
