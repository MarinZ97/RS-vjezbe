podaci_o_brojevima = {
    # Fiksni podaci
    "01":  {"vrsta": "fiksna mreža", "mjesto": "Grad Zagreb i Zagrebačka županija"},
    "020": {"vrsta": "fiksna mreža", "mjesto": "Dubrovačko-neretvanska županija"},
    "021": {"vrsta": "fiksna mreža", "mjesto": "Splitsko-dalmatinska županija"},
    "022": {"vrsta": "fiksna mreža", "mjesto": "Šibensko-kninska županija"},
    "023": {"vrsta": "fiksna mreža", "mjesto": "Zadarska županija"},
    "031": {"vrsta": "fiksna mreža", "mjesto": "Osječko-baranjska županija"},
    "032": {"vrsta": "fiksna mreža", "mjesto": "Vukovarsko-srijemska županija"},
    "033": {"vrsta": "fiksna mreža", "mjesto": "Virovitičko-podravska županija"},
    "034": {"vrsta": "fiksna mreža", "mjesto": "Požeško-slavonska županija"},
    "035": {"vrsta": "fiksna mreža", "mjesto": "Brodsko-posavska županija"},
    "040": {"vrsta": "fiksna mreža", "mjesto": "Međimurska županija"},
    "042": {"vrsta": "fiksna mreža", "mjesto": "Varaždinska županija"},
    "043": {"vrsta": "fiksna mreža", "mjesto": "Bjelovarsko-bilogorska županija"},
    "044": {"vrsta": "fiksna mreža", "mjesto": "Sisačko-moslavačka županija"},
    "047": {"vrsta": "fiksna mreža", "mjesto": "Karlovačka županija"},
    "048": {"vrsta": "fiksna mreža", "mjesto": "Koprivničko-križevačka županija"},
    "049": {"vrsta": "fiksna mreža", "mjesto": "Krapinsko-zagorska županija"},
    "051": {"vrsta": "fiksna mreža", "mjesto": "Primorsko-goranska županija"},
    "052": {"vrsta": "fiksna mreža", "mjesto": "Istarska županija"},
    "053": {"vrsta": "fiksna mreža", "mjesto": "Ličko-senjska županija"},
    # Mobilni podaci
    "091": {"vrsta": "mobilna mreža", "operater": "A1 Hrvatska"},
    "092": {"vrsta": "mobilna mreža", "operater": "Tomato"},
    "095": {"vrsta": "mobilna mreža", "operater": "Telemach"},
    "097": {"vrsta": "mobilna mreža", "operater": "bonbon"},
    "098": {"vrsta": "mobilna mreža", "operater": "Hrvatski Telekom"},
    "099": {"vrsta": "mobilna mreža", "operater": "Hrvatski Telekom"},
    # Posebne usluge
    "0800": {"vrsta": "posebne usluge"},
    "060":  {"vrsta": "posebne usluge"},
    "061":  {"vrsta": "posebne usluge"},
    "064":  {"vrsta": "posebne usluge"},
    "065":  {"vrsta": "posebne usluge"},
    "069":  {"vrsta": "posebne usluge"},
    "072":  {"vrsta": "posebne usluge"}
}

def ocisti_i_normaliziraj(broj: str) -> str | None:
    broj = "".join(ch for ch in broj if ch.isdigit() or ch == '+')
    if broj.startswith('+385'):
        broj = '0' + broj[4:]
    elif broj.startswith('00385'):
        broj = '0' + broj[5:]
    elif broj.startswith('385'):
        broj = '0' + broj[3:]
    elif not broj.startswith('0'):
        return None
    
    return broj if broj.isdigit() else None

def duljina_valjana(vrsta: str, ostatak: str) -> bool:
    return (
        (vrsta in ["fiksna mreža", "mobilna mreža"] and len(ostatak) in [6, 7])
        or (vrsta == "posebne usluge" and len(ostatak) == 6)
    )

def validiraj_broj_telefona(broj: str) -> dict:
    rezultat = {"pozivni_broj": None,
                 "broj_ostatak": None,
                 "vrsta": None,
                 "mjesto": None, 
                 "operater": None, 
                 "validan": False
                  }
    
    broj = ocisti_i_normaliziraj(broj)
    if broj is None:
        return rezultat

    for pozivni in sorted(podaci_o_brojevima, key=len, reverse=True):
        if broj.startswith(pozivni):
            ostatak = broj[len(pozivni):]
            podaci = podaci_o_brojevima[pozivni]
            if duljina_valjana(podaci["vrsta"], ostatak):
                rezultat.update({
                    "pozivni_broj": pozivni,
                    "broj_ostatak": ostatak,
                    "vrsta": podaci["vrsta"],
                    "mjesto": podaci.get("mjesto"),
                    "operater": podaci.get("operater"),
                    "validan": True
                })
            else:
                rezultat["pozivni_broj"] = pozivni
                rezultat["broj_ostatak"] = ostatak
            break
    
    return rezultat

# Primjer poziva
print(f"Primjer 1: (01) 4848-555 \nRezultat: {validiraj_broj_telefona('(01) 4848-555')}\n")
print(f"Primjer 2: +385 (91) 123 45 67 \nRezultat: {validiraj_broj_telefona('+385 (91) 123 45 67')}\n")
print(f"Primjer 3: 065 123 123 \nRezultat: {validiraj_broj_telefona('065 123 123')}\n")
