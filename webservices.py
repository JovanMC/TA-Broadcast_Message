import redis
conn = redis.Redis(host='localhost', port=6379, db=0)

condition = True
print("Redis Pubsub")


print("1. Ip Toko\n2. Aplikasi Running\n3. Kapasitas Harddisk\n4. Cek Nama Pc\n5. Keluar")
while condition == True:
    pilih = input("Pilihan :")
    if pilih == "1":
        conn.publish("toko", "1")
        print("Ip diproses")
    elif pilih =="2":
        conn.publish("toko", "2")
        print("Pengecekan Aplikasi Running diproses")
    elif pilih=="3":
        conn.publish("toko", "3")
        print("Pengecekan Kapasitas Harddisk Diproses")
    elif pilih=="4":
        conn.publish("toko", "4")
        print("Pengecekan Kapasitas Harddisk Diproses")
    else :
        condition=False

