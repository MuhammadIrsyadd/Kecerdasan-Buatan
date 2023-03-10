# Program Python untuk memeriksa apakah suatu bilangan ganjil atau genap

# Meminta input dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Memeriksa apakah bilangan ganjil atau genap
if bilangan % 2 == 0:
    print(bilangan, "adalah bilangan genap")
else:
    print(bilangan, "adalah bilangan ganjil")
