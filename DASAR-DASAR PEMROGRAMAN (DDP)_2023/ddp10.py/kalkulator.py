import math
#tambah
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
#pengurangan
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil) 
#pangkat 
def pangkat(bil1, bil2):
    hasil = bil1 ** bil2
    print("hasil pangkat dari",bil1,"^",bil2,"=", hasil)
#kali
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"x",bil2,"=",hasil) 

#bagi
def pembagian(bil1, bil2):
    hasil = bil1/bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil) 
#Log
def Log(bil):
    print('Log dari', bil, 'adalah', math.log(bil))
#sin
def sin(bil):
    print('sin dari', bil, 'adalah', math.sin(bil))
#akar
def akar(bil):
    print('akar dari', bil, 'adalah', math.sqrt(bil))
#cos
def cos(bil):
    print('cos dari', bil, 'adalah', math.cos(bil))
#tan
def tan(bil):
    print('tan dari', bil, 'adalah', math.tan(bil))