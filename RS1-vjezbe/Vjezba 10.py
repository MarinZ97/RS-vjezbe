def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    rijecnik = {}

    for rijec in rijeci:
        if rijec in rijecnik:
            rijecnik[rijec] += 1
        else:
            rijecnik[rijec] = 1
    return rijecnik

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_rijeci(tekst))