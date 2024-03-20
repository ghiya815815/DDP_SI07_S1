#1. Buat fungsi untuk menampilkan nama2 siswa yang lulus
#saja dari hasil_akhir di slide sebelumnya (nilai > 65)

def lulus_saja(hasil_akhir):
    return [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

print(lulus_saja(hasil_akhir))
#hasilnya reza dan dian



#2. Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an menggunakan for dan materi yang sudah diajarkan. (tidak boleh pakai fungsi dari python).

def balikan(buah2an):
    hasil = []
    for i in range(len(buah2an) - 1, -1, -1):
        hasil.append(buah2an[i])
    return hasil

print(balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))



#3. Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi terduplikasi.
def duplikasi(buah2an):
    hasil = []
    for buah in buah2an:
        hasil.append(buah)
        hasil.append(buah)
    return hasil

print(duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))



#4.Buat fungsi untuk membuat string baru berisi hanya konsonan dari string fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"Buat fungsi untuk membuat string baru berisi hanya konsonan dari string fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"
def hanya_konsonan(nama):
    vokal = 'aeiouAEIOU'
    hasil = ''
    for huruf in nama:
        if huruf not in vokal:
            hasil += huruf
    return hasil

print(hanya_konsonan("NurulFikri"))