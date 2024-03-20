# no 1
def profil(nama, alamat, gender, umur):
    print('nama :', nama)
    print('alamat :', alamat)
    print('Gender :', gender)
    print('umur :', umur)

profil('ghiyadhika nurhanda putri', 'bogor', 'perempuan', 18)

# no 2 (melihat nilai kelulusan)
def nilai_kelulusan(nilai : int):
    if nilai < 60:
        print('tidak lulus')
    elif nilai >= 60:
        print('lulus')
nilai_kelulusan(80)

# no 3 buat nilai sesuai paramenter bilangan(10)
def bilangan(angka):
    print('bilangan', angka)
bilangan(20)
    