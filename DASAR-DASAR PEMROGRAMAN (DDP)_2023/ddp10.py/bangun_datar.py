#segitiga
def luas_segitiga(tinggi, alas):
    hasil = (tinggi * alas) * 0.5
    print('luas segitiga dengan tinggi', tinggi, 'dan alas', alas, '=', hasil)

#persegi
def luas_persegi(sisi):
    hasil = sisi * sisi
    print('luas persegi dengan sisi', sisi, 'adalah', hasil)

#persegi panjang
def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    print('luas persegi dengan panjang', panjang, 'dan lebar', lebar, 'adalah', hasil)
    
    #belahketupat
def belah_ketupat(diagonal1, diagonal2):
    hasil = 0.5 * (diagonal1 * diagonal2)
    print('luas belah ketupat dengan diagonal 1 =', diagonal1, 'dan diagonal 2 =', diagonal2, 'adalah', hasil)
    
    #jajargenjang
def luas_jajar_genjang(panjang, lebar):
    luas = 0.5 * (panjang * lebar)
    print('luas jajar genjang dengan panjang =', panjang, 'lebar =', lebar, 'adalah', luas)

#KELILING BANGUN DATAR
def keliling_segitiga(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3 
    print('luas keliling segitiga yaitu', keliling )

def keliling_Persegi (sisi):
    hasil = sisi+sisi+sisi+sisi
    print("Keliling Persegi dengan sisi:", sisi, "adalah", hasil)

def keliling_Persegi_Panjang (panjang,lebar):
    hasil = 2*(panjang+lebar)
    print("Keliling Persegi Panjang dengan panjang:", panjang, "lebar", lebar, "adalah", hasil)
        
def keliling_JajarGenjang (a,b):
    hasil = 2*(a+b)
    print("Keliling Jajar Genjang dengan a:", a, "b:", b, "adalah", hasil)

def keliling_BelahKetupat(s1,s2,s3,s4):
    hasil = s1 + s2 + s3 + s4
    print("Keliling Belah ketupat dengan sisi 1:", s1, "sisi 2:", s2, "sisi 3:", s3, "sisi 4:", s4, "adalah", hasil)