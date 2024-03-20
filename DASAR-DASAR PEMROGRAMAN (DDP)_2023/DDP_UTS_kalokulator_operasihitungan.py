a= int(input('masukkan angka pertama = '))
b = int(input('masukkan angka kedua = '))

hitungan = input('masukkan operasi hitungan yang diinginkan = ')

if hitungan == 'kali' :
    hasilnya =a*b
elif hitungan == 'jumlah' :
    hasilnya =a+b
elif hitungan == 'kurang' :
    hasilnya =a-b
elif hitungan == 'bagi' :
    hasilnya =a/b
elif hitungan == 'pangkat' :
    hasilnya =a**b
else :
    hasilnya = 'salah'


print("angka pertama = ",a)
print("angka kedua = ",b)
print('pilihan operator = ', hitungan)
print('hasil Hitungan ',a, "x", b ,"=", hasilnya)