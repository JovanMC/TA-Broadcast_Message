import redis
conn = redis.Redis(host='localhost', port=6379, db=0)

condition = True

print("Head Office Redis")
data=[]
while condition == True:
    pilih = input("1.Kirim Pesan\n2.Keluar\nMasukan Pilihan :")
    if pilih == "1":
        title = input("Masukan Title: ")
        pesan = input("Masukan Pesan: ")
        data = []
        data.append(title)
        data.append(pesan)
        conn.publish("toko", str(data))
        print("Pesan Terkirim")
    else :
        condition=False

