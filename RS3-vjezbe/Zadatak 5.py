import asyncio

async def secure_data(data):
    await asyncio.sleep(3)
    return {
        "ime": data["ime"],
        "prezime": data["prezime"],
        "broj_kartice": hash(data["broj_kartice"]),
        "cvv": hash(data["cvv"]),
        "vrijeme": hash(data["vrijeme"])
    }

async def main():
    podaci = {
        "ime": "Pero",
        "prezime": "Perić",
        "broj_kartice": "3744 5450 3876 2503",
        "cvv": "862",
        "vrijeme": "11/29"
    }

    rezultat = await secure_data(podaci)
    print("Enkriptirani podaci:")
    print(rezultat)

asyncio.run(main())