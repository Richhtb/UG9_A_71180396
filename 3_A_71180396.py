
panjang = int(input("Masukkan panjang : "))
lebar = int(input("Masukkan lebar : "))
jariJari = int(input("Masukkan jari-jari : "))

LSemiCircle =  (3.14 * jariJari**2) / 2
LPersegiPanjang = panjang * lebar

total = (LSemiCircle + LPersegiPanjang) / 15
print (f"Area tersebut membutuhkan {round(total)} kaleng  cat")