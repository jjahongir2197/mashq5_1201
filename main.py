class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif
        self.mavjud = True


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
        print(f"{kitob.nomi} kitobi qo‘shildi.")

    def kitob_olish(self, nomi):
        for kitob in self.kitoblar:
            if kitob.nomi == nomi and kitob.mavjud:
                kitob.mavjud = False
                print(f"{nomi} kitobi berildi.")
                return
        print("Kitob mavjud emas.")

    def kitoblar_royxati(self):
        print("Kutubxonadagi kitoblar:")
        for kitob in self.kitoblar:
            holat = "Mavjud" if kitob.mavjud else "Olingan"
            print(f"{kitob.nomi} - {kitob.muallif} ({holat})")


k1 = Kitob("Python Asoslari", "Guido")
k2 = Kitob("Algoritmlar", "Knuth")

kutubxona = Kutubxona()
kutubxona.kitob_qoshish(k1)
kutubxona.kitob_qoshish(k2)

kutubxona.kitoblar_royxati()
kutubxona.kitob_olish("Python Asoslari")
kutubxona.kitoblar_royxati()
