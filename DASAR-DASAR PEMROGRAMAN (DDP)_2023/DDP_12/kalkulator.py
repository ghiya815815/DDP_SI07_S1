 #2
 # Definisikan fungsi untuk menghitung luas dan keliling persegi
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

# Definisikan fungsi untuk menghitung luas dan keliling lingkaran
import math

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

# Menu aplikasi
print("Selamat datang di Aplikasi Rumus Bangun Datar")
print("Pilih bangun datar yang ingin dihitung:")
print("1. Persegi")
print("2. Lingkaran")

pilihan = input("Masukkan pilihan Anda (1/2): ")

if pilihan == '1':
    sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
    print(f"Luas persegi: {luas_persegi(sisi_persegi)}")
    print(f"Keliling persegi: {keliling_persegi(sisi_persegi)}")
elif pilihan == '2':
    jari_jari_lingkaran = float(input("Masukkan panjang jari-jari lingkaran: "))
    print(f"Luas lingkaran: {luas_lingkaran(jari_jari_lingkaran)}")
    print(f"Keliling lingkaran: {keliling_lingkaran(jari_jari_lingkaran)}")
else:
    print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")