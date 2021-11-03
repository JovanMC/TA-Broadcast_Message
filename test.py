import re
str = "Selamat Belajar PYTHON"
exc = re.search("\s", str)
print("Karakter spasi putih pertama berada di:", exc.start())