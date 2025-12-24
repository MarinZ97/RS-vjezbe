import asyncio
from aiohttp import web
from aiohttp import ClientSession


CATFACT_URL = "https://catfact.ninja/fact"

async def fetch_fact(session):
    async with session.get(CATFACT_URL) as resp:
        data = await resp.json()
        return data.get("fact", "")

async def get_facts(amount):
    async with ClientSession() as session:
        tasks = [fetch_fact(session) for _ in range(amount)]
        return await asyncio.gather(*tasks)

async def cats(request):
    try:
        amount = int(request.query.get("amount"))
    except (TypeError, ValueError):
        return web.json_response(
            {"Error": "amount mora biti cijeli broj"},
            status = 400
        )

    if amount <= 0:
        return web.json_response(
            {"Error": "amount mora biti > 0"},
            status = 400
        )

    facts = await get_facts(amount)
    return web.json_response({"facts": facts})

app = web.Application()
app.router.add_get("/cat", cats)

web.run_app(app, port=8086)