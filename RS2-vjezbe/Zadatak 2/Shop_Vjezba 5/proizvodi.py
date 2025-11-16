class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
        
    def ispis(self):
        print(f"Naziv proizvoda: {self.naziv}")
        print(f"Cijena: {self.cijena} EUR")
        print(f"Dostupna količina: {self.dostupna_kolicina} komada")

skladiste = []

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
   proizvod = Proizvod(naziv, cijena, dostupna_kolicina)
   skladiste.append(proizvod)