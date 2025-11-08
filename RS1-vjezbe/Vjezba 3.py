import random

trazeni_broj = random.randint(1, 100)
broj_pokusaja = 0
broj_je_pogoden = False

print("Pogodite broj između 1 i 100.")

while not broj_je_pogoden:
        unos = int(input("Unesite vaš pokušaj: "))
        broj_pokusaja += 1
        
        if unos < trazeni_broj:
            print("Broj je veći od unesenog.")
        elif unos > trazeni_broj:
            print("Broj je manji od unesenog.")
        else:
            broj_je_pogoden = True
            print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")
