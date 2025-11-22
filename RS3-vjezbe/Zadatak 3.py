import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]


baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik):
    await asyncio.sleep(2) 
    for zapis in baza_lozinka:
        if zapis["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            if zapis ["lozinka"] == korisnik["lozinka"]:
                return "Autorizacija uspješna"
            else:
                return "Autorizacija neuspješna"
    return "Lozinka nije pronađena"

async def autentifikacija(korisnik):
    await asyncio.sleep(3) 
    for zapis in baza_korisnika:
        if zapis["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            return await autorizacija(korisnik)
    return "Korisnik nije pronađen"

async def main_task():
    test = {
        'korisnicko_ime': 'maja_0x',
        'email': 'majaaaaa@gmail.com',
        'lozinka': 's324SDFfdsj234'
    }
    
    rezultat = await autentifikacija(test)
    print(rezultat)

asyncio.run(main_task())

