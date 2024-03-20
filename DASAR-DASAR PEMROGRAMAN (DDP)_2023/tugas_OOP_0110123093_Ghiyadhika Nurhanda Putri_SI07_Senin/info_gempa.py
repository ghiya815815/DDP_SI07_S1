from gempa import *
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

gempa1.dampak() # Output: Dampak gempa tidak berasa
gempa2.dampak() # Output: Dampak gempa bangunan roboh dan berpotensi tsunami
gempa3.dampak() # Output: Dampak gempa bangunan roboh
gempa4.dampak() # Output: Dampak gempa tidak berasa
gempa5.dampak() # Output: Dampak gempa bangunan roboh
    