# Program Python untuk menghitung faktorial suatu bilangan menggunakan rekursi

def faktorial(n):
   if n == 1:
       return n
   else:
       return n * faktorial(n-1)

# Meminta input dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Periksa apakah bilangan negatif atau positif
if bilangan < 0:
   print("Maaf, faktorial tidak tersedia untuk bilangan negatif")
elif bilangan == 0:
   print("Faktorial dari 0 adalah 1")
else:
   print("Faktorial dari", bilangan, "adalah", faktorial(bilangan))
