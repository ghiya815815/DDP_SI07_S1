class Kucing:
    nama = ''
    warna = ''
    umur = 0
    
    lapar = True
    #konstruksi
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
    #def
    def makan(self):
        self.lapar = False
        
    #method
    def tampilkan_data_diri(self):
        print(f"nama : {self.nama}")
        print(f"warna : {self.warna}")
        print(f"umur : {self.umur}")
        print(f"lapar : {self.lapar}")
        
        
    
omeng = Kucing('omeng', 'merah',6)
dede = Kucing('dede', 'item', 7)

omeng.tampilkan_data_diri()
omeng.makan()
omeng.tampilkan_data_diri()

omeng.umur += 1
print(omeng.umur)


    