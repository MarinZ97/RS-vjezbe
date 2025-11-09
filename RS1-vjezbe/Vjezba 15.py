def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_brojac = 0
    consonants_brojac = 0

    for char in tekst:
            if char in vowels:
                vowel_brojac += 1
            elif char in consonants:
                consonants_brojac += 1
    return vowel_brojac, consonants_brojac

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))