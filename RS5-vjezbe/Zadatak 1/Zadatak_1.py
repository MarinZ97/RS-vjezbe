from aiohttp import web

PROIZVODI = [
    {"naziv": "Kava", "cijena": 2.50, "kolicina": 30},
    {"naziv": "Caj", "cijena": 3.00, "kolicina": 20},
    {"naziv": "Sok", "cijena": 4.00, "kolicina": 10},
]

async def get_proizvodi(request: web.Request) -> web.Response:
    return web.json_response(PROIZVODI)

def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    return app

if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8081)
