# deklarasi function
def kampus_saya():
    print('STT nurul fikri')
    print('si1')
    
#function argumen  setelah anama fungsi, bisa ditambah dengann spasi di dalam tanda kurung 
def hello(nama, alamat, no_tlp):
    print('helo nama saya adalah', nama)
    print('alamat saya di', alamat)
    print('no_tlp saya adalah', no_tlp)

hello('ghiyadhika', 'bogor', 3469)

#dipanggilnya
kampus_saya() 
kampus_saya()
# setiap kali kita manggil baru akan di print 

#argumen
def nama_fungsi(nama = 'ahmad'):
    print ('nama saya adalah ', nama)

nama_fungsi('armad')
nama_fungsi('acmad')
nama_fungsi()

def perkalian_dua(x):
    return x * 2;

print(perkalian_dua(5))
