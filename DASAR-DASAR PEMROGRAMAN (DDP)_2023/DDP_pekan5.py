#1. Buat list untuk menampilkan data pada kategori kendaraan 

kendaraan1 = ["avansa", "mobil", "Toyota", 1500]
print(kendaraan1)

#2. Dari no 1 ditambahkan dari list yang sudah ada
#[warna kendaraan, jml kendaraan, harga kendaraan]
# di hapus jenis kendaraanya 

kendaraan1 = kendaraan1 + ["hitam",4, 250_000_000]
print(kendaraan1)
kendaraan1.remove("mobil")
print(kendaraan1)

#3. Buat dengan match case
pesan = """
menu:
1. menghitung luas persegi
2. menghitung lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan = input(pesan)

match pilihan:
 case "1":
  print("anda memasukkan angka 1 untuk menghitung luas persegi")
  sisi = int(input ("masukan sisi:"))
  luas = sisi * sisi
  print("luas persegi yang sisinya", sisi, "adalah", luas)
 case "2":
  print ("kamu memilih 2 untuk menghitung luas lingkaran")
  jari_jari= int(input ("masukan jari_jari:"))
  luas = 3,14 * jari_jari **2
  print ("luas lingkaran yang jari_jari", jari_jari, "adalah", luas)
 case "3":
  print ("anda memasukan angka 3 untuk menghitung luas segitiga ")
  alas = int(input("masukan alas:"))
  tinggi = int(input("masukan tinggi:"))
  luas = 1/2 * alas * tinggi
  print ("luas segitiga alasnya", alas, " dan tingginya", tinggi, "adalah ", int(luas))

#print keterangan dan hasil luas 

 case _:
  print("inputan tidak valid")