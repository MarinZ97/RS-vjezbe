import asyncio
from aiohttp import web, ClientSession

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Mis", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slusalice", "cijena": 50},
]

narudzbe = []

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def get_proizvod(request):
    proizvod_id = int(request.match_info["id"])
    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)

    if proizvod is None:
        return web.json_response(
            {"error": "Proizvod sa traženim ID-em ne postoji"},
            status=404
        )

    return web.json_response(proizvod)

async def post_narudzba(request):
    data = await request.json()
    proizvod_id = data["proizvod_id"]
    kolicina = data["kolicina"]

    proizvod = next((p for p in proizvodi if p["id"] == proizvod_id), None)
    if proizvod is None:
        return web.json_response(
            {"error": "Proizvod sa traženim ID-em ne postoji"},
            status=404
        )
    narudzbe.append({
        "proizvod_id": proizvod_id,
        "kolicina": kolicina
    })

    return web.json_response(narudzbe)

def create_app():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvod)
    app.router.add_post("/narudzbe", post_narudzba)
    return app

async def main():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()

    async with ClientSession() as session:
        await session.post("http://localhost:8081/narudzbe",
                           json = {"proizvod_id": 1, "kolicina": 2})

        async with session.get("http://localhost:8081/proizvodi") as r:
            print("Proizvodi:", await r.json())

        async with session.post("http://localhost:8081/narudzbe",
                               json = {"proizvod_id": 99, "kolicina": 1}) as r:
            print("Greška:", await r.json())

    await runner.cleanup()

asyncio.run(main())
