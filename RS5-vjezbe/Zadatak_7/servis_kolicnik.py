from aiohttp import web

async def kolicnik(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Mora biti validan JSON."}, status=400)

    if not isinstance(data, dict) or "zbroj" not in data or "umnozak" not in data:
        return web.json_response({"error": "Očekujemo JSON s poljima zbroj i umnozak."}, status=400)

    zbroj = data["zbroj"]
    umnožak = data["umnozak"]

    if not isinstance(zbroj, (int, float)) or not isinstance(umnožak, (int, float)):
        return web.json_response({"error": "zbroj i umnozak moraju biti brojevi."}, status=400)

    if zbroj == 0:
        return web.json_response({"error": "Dijeljenje s 0 nije dozvoljeno."}, status=400)

    return web.json_response({"kolicnik": umnožak / zbroj})

app = web.Application()
app.router.add_post("/kolicnik", kolicnik)

web.run_app(app, port=8085)
