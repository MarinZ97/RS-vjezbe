def filtriraj_parne(lista):
    parni = []
    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
    return parni

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))