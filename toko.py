import smtplib
import redis
import ast
import os

# untuk membuat koneksi ke redis
conn = redis.Redis(host='localhost', port=6379, db=0)
p = conn.pubsub()
p.subscribe('toko')

while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        data = message['data'].decode('utf-8')
        print(data)
        # value = ast.literal_eval(data)  # untuk mengubah string menjadi list menggunakan ast
        if data == "1":
            result = os.system("ipconfig")
            print(result)
        elif data == "2":
            result = os.system("""tasklist/fi "STATUS eq running""""")
            print(result)
        elif data =="3":
            result = os.system("")
        elif data =="4":
            result = os.system("hostname")