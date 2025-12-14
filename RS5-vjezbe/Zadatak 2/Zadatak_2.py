from aiohttp import web

PROIZVODI = [
    {"naziv": "Kava", "cijena": 2.50, "kolicina": 30},
    {"naziv": "Caj", "cijena": 3.00, "kolicina": 20},
    {"naziv": "Sok", "cijena": 4.00, "kolicina": 10},
]

async def get_proizvodi(request: web.Request) -> web.Response:
    return web.json_response(PROIZVODI)

async def post_proizvodi(request: web.Request) -> web.Response:
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"greska: Body mora biti validan JSON"}, status = 400)

    obavezno = {"naziv", "cijena", "kolicina"}
    if not obavezno.issubset(data.keys()):
        return web.json_response(
            {"greska": "JSON mora sadrzavati: naziv, cijena, kolicina."},
            status = 400,
            )

    print("Primljen proizvod:", data)

    novi_proizvodi = {
        "naziv" : data["naziv"],
        "cijena" : data["cijena"],
        "kolicina" : data["kolicina"],
    }

    PROIZVODI.append(novi_proizvodi)
    return web.json_response(PROIZVODI)

def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_post("/proizvodi", post_proizvodi)
    return app

if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8081)
