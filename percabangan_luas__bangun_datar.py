#jenis bangun datar
print("1. luas persegi")
print("2. luas persegi panjang")
print("3. luas seitiga")
print("4. luas lingkaran")
#pilih bangun datar
pilihan = int(input("pilih salah satu bangun datar tersebut: "))
#rumus yang akan di gunakan
if (pilihan == 1):
    sisi = int(input("panjang sisi= "))
    luas = sisi*sisi
    print("1. luas persegi= ", luas)

elif (pilihan == 2):
    panjang = int(input("panjang= "))
    lebar = int(input("lebar= "))
    luas = panjang*lebar
    print("2. luas persegi panjang= ",luas)

elif (pilihan == 3):
    alas = int(input("alas= "))
    tinggi = int(input("tinggi= "))
    luas = (1/2) * alas*tinggi
    print("3. luas segitiga= ", luas)

elif (pilihan == 4):
    r = int(input("r= "))
    luas = (22/7)*r
    print("4. luas lingkaran= ", luas)

else : 
    print ("sorry, invalid input")


