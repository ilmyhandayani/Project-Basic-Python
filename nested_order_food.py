print("===== Selamat datang di resto kami =====")
print("silahkan pesan menu yang anda inginkan")
pesan = input("apakah anda ingin memesan [y/n]:")
if pesan == "y":
    makanan = input("apakah anda ingin membeli makanan berat [y/n]:")
    if makanan == "y":
        print("menu makanan kami")
        print("1. nasi  \n2. ayam \n3. ikan \n4. bebek \n5. mie")
        makan = input("silahkan pilih menu di atas:")
        if makan == 1:
            print("1. nasi goreng biasa \n2. nasi bakar \n3. nasi uduk \n4. nasi goreng spesial \n5. nasi goreng polosan \n6. Nasi kuning")
            nasi = input("silahkan pilih nasi di atas:")
            if nasi == 1:
                nasi1 = 15000
                print("Nasi Goreng Biasa \nHarga Rp", nasi1)
            elif nasi == 2:
                nasi2 = 10000
                print("Nasi Bakar \nHarga Rp", nasi2)
            elif nasi == 3:
                nasi3 = 8000
                print("Nasi Uduk \nHarga Rp", nasi3)
            elif nasi == 4:
                nasi4 = 20000
                print("Nasi Goreng Biasa \nHarga Rp",nasi4)
            elif nasi == 5:
                nasi5 = 10000
                print("Nasi Goreng Biasa \nHarga Rp", nasi5)
            elif nasi == 6:
                nasi6 = 10000
                print("Nasi Kuning \nHarga Rp", nasi6)
        elif makan == 2:
            print("1. ayam bakar \n2. ayam goreng \n3. ayam kecap")
            ayam = int(input("pilih manu di atas:"))
            if ayam == 1:
                ayam1 = 20000
                print("Ayam Bakar \nHarga Rp", ayam)
            elif ayam == 2:
                ayam2 = 18000
                print("Ayam Goreng \nHarga Rp", ayam2)

else :
    print("yahh... kenapa gajadi pesan, cobain dulu masakan kami dijamin nikmat deh.....")
