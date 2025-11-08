def brojanje_riječi(tekst):
    riječi = tekst.split()
    frekvencija = {}
    
    for riječ in riječi:
        if riječ in frekvencija:
            frekvencija[riječ] += 1
        else:
            frekvencija[riječ] = 1
    return frekvencija

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))