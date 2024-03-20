class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif 4 <= self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        else:
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")

# Test Case
gempa1 = Gempa("Sumatra", 3.5)
gempa1.dampak() # Output: Dampak gempa bangunan retak-retak

gempa2 = Gempa("Bali", 7.5)
gempa2.dampak() # Output: Dampak gempa bangunan roboh dan berpotensi tsunami