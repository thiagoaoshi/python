import mysql.connector
from flask import Flask

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="database-nome",
  )
mycursor = mydb.cursor()
  # mycursor.execute("SELECT * FROM tb_dados")
sql = "SELECT * FROM tb_dados ORDER BY nome"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
app = Flask(__name__)

@app.route('/')
def lista_deploy():
    return x

if __name__ == '__main__':
    app.run()
