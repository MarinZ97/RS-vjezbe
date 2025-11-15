from datetime import datetime
import math

# Zadatak 1
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraža} km")
    
    def starost(self):
        trenutna_godina = datetime.now().year
        starost_godine = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost_godine} godina.")

auto = Automobil("Skoda", "Octavia", 2018, 25000)
print("Zadatak 1: Automobil")
auto.ispis()
auto.starost()

# Zadatak 2
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b
    def oduzimanje(self):
        return self.a - self.b
    def mnozenje(self):
        return self.a * self.b
    def dijeljenje(self):
        return self.a / self.b
    def potenciranje(self):
        return self.a ** self.b
    def korijen(self):
        korijen_a = math.sqrt(self.a)
        korijen_b = math.sqrt(self.b)
        return f"Korjen iz {self.a}: {korijen_a}, Korijen iz {self.b}: {korijen_b}"

kalk = Kalkulator(16, 4)
print("\nZadatak 2: Kalkulator")
print(f"Zbroj:{kalk.zbroj()}")
print(f"Oduzimanje:{kalk.oduzimanje()}")
print(f"Množenje:{kalk.mnozenje()}")
print(f"Dijeljenje:{kalk.dijeljenje()}")
print(f"Potenciranje:{kalk.potenciranje()}")
print(f"Korijen:{kalk.korijen()}")

# Zadatak 3
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek_ocjena(self):
        sum_ocjena = sum(self.ocjene)
        if len(self.ocjene) == 0:
            return 0
        return sum_ocjena / len(self.ocjene)
    
    def ispis(self):
        print(f"\nIme:{self.ime}")
        print(f"Prezime:{self.prezime}")
        print(f"Godine:{self.godine}")
        print(f"Ocjene:{self.ocjene}")
    
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []
for student in studenti:
    studenti_objekti.append(Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]))

print("\nZadatak 3: Prosjek ocjena i najbolji student")

for student in studenti_objekti:
    student.ispis()

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek_ocjena())
print(f"Najbolji student je: {najbolji_student.ime} {najbolji_student.prezime} sa prosjekom ocjena {najbolji_student.prosjek_ocjena():.2}")

# Zadatak 4
class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return self.r * math.pi
    
    def povrsina(self):
        return self.r ** 2 * math.pi

krug_objekt = Krug(r=4)
print("\nZadatak 4: Krug")
print(f"Opseg kruga je: {krug_objekt.opseg():.2f}")
print(f"Površina kruga je: {krug_objekt.povrsina():.2f}")

# Zadatak 5
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"{self.ime} radi na poziciji: {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, odjel):
        super().__init__(ime, pozicija, placa)
        self.odjel = odjel

    def work(self):
        print(f"{self.ime} radi na poziciji {self.pozicija} u odjelu {self.odjel}")

    def povisica(self, radnik, iznos):
        radnik.placa += iznos
        print(f"Voditelj {self.ime} je dao povišicu radniku {radnik.ime} za {iznos} EUR-a")

print("\nZadatak 5: Radnik i Manager")
radnik1 = Radnik("Petar", "Programer", 2000)
manager1 = Manager("Ivan", "Voditelja", 3000, "Razvoj")

radnik1.work()
manager1.work()
manager1.povisica(radnik1, 300)