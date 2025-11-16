from proizvodi import dodaj_proizvod, skladiste
from narudzbe import Narudzba

proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    dodaj_proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])

print("Skladište")
for proizvod in skladiste:
    proizvod.ispis()

narudzba = Narudzba()

print("\nDodavanje u narudžbu:")
narudzba.napravi_narudzbu(skladiste[0], 3)
narudzba.napravi_narudzbu(skladiste[1], 1)
narudzba.napravi_narudzbu(skladiste[2], 4)
narudzba.napravi_narudzbu(skladiste[3], 3)

narudzba.ispis()

