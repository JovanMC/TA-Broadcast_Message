import redis
import pickle
import re

conn = redis.Redis(host='localhost', port=6379, db=0)

# data = {"kategori":"Pengumuman","message":"Kepada seluruh karyawan yang terkasih"}
# p_data = pickle.dumps(data)
# conn.set('message[1]',p_data)

read_dict = conn.get('message[1]')
yourdict = pickle.loads(read_dict)

# dictionary_items = yourdict.items()

# for item in dictionary_items:
#     print(item[1])

dataKey = conn.keys("*")
print(dataKey[len(dataKey)-1])
data = dataKey[len(dataKey)-1].decode('utf-8')


a = re.findall("\d",data)
print(int(a[0]))








