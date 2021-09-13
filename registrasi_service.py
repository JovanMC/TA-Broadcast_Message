from flask import Flask
import ast

import redis
import mysql.connector
app = Flask(__name__)

# untuk menerima message dari redis dan mmebuat koneksi
conn = redis.Redis(host='localhost', port=6379, db=0)
p = conn.pubsub()
p.subscribe('register')

#membuat koneksi db mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ta"
)

# untuk mengirim data ke tbl_registrasi
while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        data = message['data'].decode('utf-8')
        value = ast.literal_eval(data) # untuk mengubah string menjadi list menggunakan ast
        print(value)
        mycursor = mydb.cursor()
        mycursor.execute('insert into tbl_registrasi (id,name,email,password) values (default,%s,%s,%s)', (value[0],value[1],value[2]))
        mydb.commit()
        mycursor.close()