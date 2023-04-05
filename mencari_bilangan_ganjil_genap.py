#masukan bilangan
bil = int(input("Masukan Bilangan :"))
#cek bilangan, jika bernilai true tampilkan output genap, jika false tampilkan output ganjil
if bil % 2 == 0:
    print(" %d Merupakan Bilangan Genap" % bil)
else:
    print("%d Merupakan Bilangan Ganjil" % bil)
#selesai