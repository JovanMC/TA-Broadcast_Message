import os
import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

result = os.system("ipconfig")
result = str(result)
print(type(result))

conn.set("toko1", f"{result}" )
print(conn.get("toko1"))