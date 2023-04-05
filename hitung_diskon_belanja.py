#masukan total belanja
total = int(input('masukan total belanjaan anda: '))
setelah_diskon = total
#cek diskon sesuai harga
if total > 500000:
    diskon = total * (20/100)
elif total > 300000:
    diskon = total * (10/100)
elif total > 150000:
    diskon = total * (5/100)
else :
    diskon = total * (0/100)
#hasil/output
setelah_diskon = total - diskon
print("Anda mendapatkan diskon: Rp {:,}".format(int(diskon)).replace(',','.'))
print("Harga setelah mendapatkan diskon: Rp {:,}".format(int(setelah_diskon)).replace(',','.'))
#selesai