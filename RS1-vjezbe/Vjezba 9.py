def ukloni_duplikate(lista):
    nova_lista = []
    skup = set()
    for broj in lista:
        if broj not in skup:
            nova_lista.append(broj)
            skup.add(broj)
    return nova_lista

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))