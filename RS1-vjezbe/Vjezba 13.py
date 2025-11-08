# zadatak 1
def prvi_i_zadnji(lista):
    return lista[0], lista[-1]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista)) 

# zadatak 2
def maks_i_min(lista):
    maks = lista[0]
    min = lista[0]

    for broj in lista[1:]:
        if broj > maks:
            maks = broj
        if broj < min:
            min = broj
    return maks, min

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista)) 

# zadatak 3
def presjek(skup_1, skup_2):
    return skup_1 & skup_2

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2)) 