from aiohttp import web

def validate_brojevi(data):
    if not isinstance(data, dict) or "brojevi" not in data:
        return False, web.json_response({"error": "Nedostaje polje: brojevi."}, status=400)
    if not isinstance(data["brojevi"], list) or len(data["brojevi"]) == 0:
        return False, web.json_response({"error": "brojevi moraju biti lista s minimalno jednim brojem."}, status=400)
    for x in data["brojevi"]:
        if not isinstance(x, (int, float)):
            return False, web.json_response({"error": "Svi elementi moraju biti brojevi."}, status=400)
    return True, None

async def umnozak(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Treba biti validan JSON."}, status=400)

    ok, error = validate_brojevi(data)
    if not ok:
        return error

    umnozak = 1
    for x in data["brojevi"]:
        umnozak *= x

    return web.json_response({"umnozak": umnozak})

app = web.Application()
app.router.add_post("/umnozak", umnozak)

web.run_app(app, port=8084)
