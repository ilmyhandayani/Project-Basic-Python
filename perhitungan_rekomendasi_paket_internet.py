print("\n======Rekomendasi Paket Internet======")
print("=== Ada 4 jenis paket yang tersedia ===")

print("1. paket premium 70 hari ")
print("2. paket premium 50 hari ")
print("3. paket ekonomi 70 hari ")
print("4. paket ekonomi 50 hari ")
print()

gaji_andi = int(input("masukan gaji andi perbulan: "))
gaji_perhari = gaji_andi/30 
paket_premium1 = 620000
paket_premium2 = 410000
paket_ekonomi1 = 380000
paket_ekonomi2 = 220000

if (gaji_andi):
   
    #paket premium 70 hari
    print("\n=== Rincian dan sisa uang paket premium 70 hari ===")
    paket_premium70 = gaji_perhari*70-paket_premium1 
    print("harga paket premium 70 hari adalah Rp ", paket_premium1)
    print("gaji andi selama 70 hari adalah Rp ", gaji_perhari*70)
    print("sisa uang andi jika membeli paket ini yaitu Rp ", paket_premium70)
   
    #paket premium 50 hari
    print("\n=== Rincian dan sisa uang paket premium 50 hari ===")
    paket_premium50 = gaji_perhari*50-paket_premium2
    print("harga paket premium 50 hari adalah Rp ", paket_premium2)
    print("gaji andi selama 50 hari adalah Rp ", gaji_perhari*50)
    print("sisa uang andi jika membeli paket ini yaitu Rp ", paket_premium50)
   
    #paket ekonomi 70 hari 
    print("\n=== Rincian dan sisa uang paket ekonomi 70 hari ===")
    paket_ekonomi70 = gaji_perhari*70-paket_ekonomi1
    print("harga paket ekonomi 70 hari adalah Rp ", paket_ekonomi1)
    print("gaji andi selama 70 hari adalah Rp ", gaji_perhari*70)
    print("sisa uang andi jika membeli paket ini adalah Rp ", paket_ekonomi70)
  
    #paket ekonomi 70 hari 
    print("\n=== Rincian dan sisa uang paket ekonomi 50 hari ===")
    paket_ekonomi50 = gaji_perhari*50-paket_ekonomi2
    print("harga paket ekonomi 50 hari adalah Rp ", paket_ekonomi2)
    print("gaji andi selama 50 hari adalah Rp ", gaji_perhari*50)
    print("sisa uang andi jika membeli paket ini adalah Rp ", paket_ekonomi50)

    print("\n=== paket paling rekomemded adalah paket ekonomi 50 hari ===")

