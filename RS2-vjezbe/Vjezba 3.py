import math
# Zadatak 1
parni_kvadrati = [x**2 for x in range(20,51) if (x**2) % 2 == 0]
print(parni_kvadrati)

# Zadatak 2
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(x) for x in rijeci if 'a' in x]
print(duljine_sa_slovom_a)

# Zadatak 3
brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kubovi = [{x: x**3} if x % 2 != 0 else {x: x} for x in brojevi]
print(kubovi)

# Zadatak 4
korijeni = {x: round(math.sqrt(x), 2) for x in range (50, 501, 50)}
print(korijeni)

# Zadatak 5
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi)

# Zadatak 6
brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
faktorijeli = {x: [math.factorial(y) for y in range(1, x + 1)] 
               for x in brojevi}
print(faktorijeli)