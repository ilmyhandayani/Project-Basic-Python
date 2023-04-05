ulang = "y"
while (ulang !="t"):
    print("Pilihan")
    print("\t1. Konversi Rupiah ke Dollar")
    print("\t2. Konversi Dollar ke Rupiah")

    pilih = int(input("\nPilihanmu: "))

    if pilih == 1:
        nilaiRupiah = int(input("\nMasukan nilai Rupiah = Rp."))
        konversiDollar = nilaiRupiah/15000
        print("Jumlah Konversi ke Dollar = $", konversiDollar)
    elif pilih == 2:
        nilaiDollar = int(input("\nMasukan niali Dollar = $"))
        konversiRupiah = nilaiDollar*15000
        print("Jumlah Konversi ke Rupiah = Rp.",konversiRupiah)
    else:
        print("Maaf pilihan ini tidak tersedia")

    ulang = input("Ingin ulang lagi?(y/t):")

print("-----SELESAI-----")