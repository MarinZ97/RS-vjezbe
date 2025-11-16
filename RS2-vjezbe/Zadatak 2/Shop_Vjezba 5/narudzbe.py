class Narudzba:
    def __init__(self):
        self.naruceni_proizvodi = {}
        self.ukupna_cijena = 0

    def napravi_narudzbu(self, proizvod, kolicina):

        if kolicina <= 0:
            print("Greška: količina mora biti veća od 0")
            return

        if kolicina > proizvod.dostupna_kolicina:
            print(f"Greška: tražena količina '{proizvod.naziv}' nije dostupna.")
            return

        if proizvod in self.naruceni_proizvodi:
            stara_kolicina = self.naruceni_proizvodi[proizvod]
            nova_kolicina = stara_kolicina + kolicina
            self.naruceni_proizvodi[proizvod] = nova_kolicina
        else:
            self.naruceni_proizvodi[proizvod] = kolicina

        proizvod.dostupna_kolicina = proizvod.dostupna_kolicina - kolicina

        cijena_za_dodati = proizvod.cijena * kolicina
        self.ukupna_cijena = self.ukupna_cijena + cijena_za_dodati

    def ispis(self):
        print("\nNarudžba")
        for proizvod, kol in self.naruceni_proizvodi.items():
            print(f"Proizvod: {proizvod.naziv}, Količina: {kol}, Cijena: {proizvod.cijena * kol} EUR")
        print(f"Ukupna cijena narudžbe: {self.ukupna_cijena} EUR\n")
