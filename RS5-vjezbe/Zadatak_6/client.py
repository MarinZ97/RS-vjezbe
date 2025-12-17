import asyncio
from aiohttp import ClientSession

async def posalji_zahtjev(url, port):
    adresa = f"http://{url}:{port}/pozdrav"
    async with ClientSession() as session:
        async with session.get(adresa) as response:
            return await response.json()

async def main():
    print("Sekvencijalno:")
    rezultat1 = await posalji_zahtjev("localhost", 8081)
    print(rezultat1)

    rezultat2 = await posalji_zahtjev("localhost", 8082)
    print(rezultat2)

    print("\nKonkurentno:")
    rezultati = await asyncio.gather(
        posalji_zahtjev("localhost", 8081),
        posalji_zahtjev("localhost", 8082)
    )

    for request in rezultati:
        print(request)

asyncio.run(main())
