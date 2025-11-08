def obrni_rjecnik(rjecnik):
    obrnut_rjecnik = {}
    for ključ, vrijednost in rjecnik.items():
        obrnut_rjecnik[vrijednost] = ključ  
    return obrnut_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))