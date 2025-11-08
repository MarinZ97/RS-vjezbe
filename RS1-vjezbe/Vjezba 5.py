for i in range(1, 2):
    print(i)

    # Ova petlja nema smisla jer se petlja mora minimalno dva puta pokrenuti.
    # U gornjem kodu, petlja će se izvršiti samo jednom (za i=1).


for i in range(10, 1, 2):
    print(i)

    # Ništa neće ispisati, jer nema uvjeta koji bi omogućio ponavljanje.
    # 10 je start, 1 je stop/kraj, a 2 je koliko pomaka napravi svaki put.
    # Da je stavljen -2 za pomak onda bi krenulo ispisivati od 10 prema 2.

for i in range(10, 1, -1):
    print(i)

    # Petlja broji unazad od 10 do 2 i ispisuje svaki broj.
    # Znači ispisat će 10, 9, 8, 7, 6, 5, 4, 3, 2.