# buat class animal sebagai parent class, class animal mempunyai 4 properti (name,mkanan, hidup, berkembang biak)
# buat minimal 3 class child (badak,ikan, ular, dll) setiap child itu memiliki 2 properti dan metode


class Animal:
    def __init__(self, name, mkanan, hidup, berkembang_biak):
        self.name = name
        self.mkanan = mkanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print(f"{self.name} adalah {self.mkanan}. Hidupnya: {self.hidup}. Berkembang biaknya: {self.berkembang_biak}")


class Badak(Animal):
    def __init__(self, name, mkanan, hidup, berkembang_biak, berat_badan):
        super().__init__(name, mkanan, hidup, berkembang_biak)
        self.berat_badan = berat_badan

    def cetak(self):
        super().cetak()
        print(f"Berat badan {self.name}: {self.berat_badan} kg")


class Ikan(Animal):
    def __init__(self, name, mkanan, hidup, berkembang_biak, panjang_badan):
        super().__init__(name, mkanan, hidup, berkembang_biak)
        self.panjang_badan = panjang_badan

    def cetak(self):
        super().cetak()
        print(f"Panjang badan {self.name}: {self.panjang_badan} m")


class Ular(Animal):
    def __init__(self, name, mkanan, hidup, berkembang_biak, panjang_ulang):
        super().__init__(name, mkanan, hidup, berkembang_biak)
        self.panjang_ulang = panjang_ulang

    def cetak(self):
        super().cetak()
        print(f"Panjang ulang {self.name}: {self.panjang_ulang} cm")
        

class Singa(Animal):
    def __init__(self, name, mkanan, hidup, berkembang_biak, berat_badan):
        super().__init__(name, mkanan, hidup, berkembang_biak)
        self.berat_badan = berat_badan
    def cetak(self):
        super().cetak()
        print(f"Berat badan {self.name}: {self.berat_badan} kg")
        

# methode 
b = Badak("badak bercula 1", " Herbivora", "di hutan", "melahirkan", 950)
b.cetak()

i = Ikan("Hiu", "Karnivora", "Laut", "bertelur dan beranak", 6)
i.cetak()

u = Ular("Anaconda", "Karnivora", "di hutan", "bertelur", 6)
u.cetak()

s = Singa("Singa", "Karnivora", "di hutan", "melahirkan", 190)
s.cetak()