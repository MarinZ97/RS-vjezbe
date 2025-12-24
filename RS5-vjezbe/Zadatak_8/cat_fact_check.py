from aiohttp import web

async def facts(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"Error": "Zahtjev mora biti validan."}, status = 400)

    if not isinstance(data, dict) or "facts" not in data or not isinstance(data["facts"], list):
        return web.json_response({"Error": "Očekujemo JSON oblika {'facts': [ ... ]}."}, status = 400)

    filtered = []
    for fact in data["facts"]:
        if not isinstance(fact, str):
            continue

        tekst = fact.lower()
        if "cat" in tekst:     
            filtered.append(fact)

    return web.json_response({"facts": filtered})

app = web.Application()
app.router.add_post("/facts", facts)

web.run_app(app, port=8087)