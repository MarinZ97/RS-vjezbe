import asyncio
from aiohttp import ClientSession

async def post_json(session, url, payload):
    async with session.post(url, json=payload) as response:
        content = response.headers.get("Content-Type", "")
        if "application/json" in content:
            data = await response.json()
        else:
            data = {"raw": await response.text()}
        return response.status, data

async def main():
    brojevi = [3, 4, 5]
    payload = {"brojevi": brojevi}

    url_sum = "http://localhost:8083/zbroj"
    url_mul = "http://localhost:8084/umnozak"
    url_div = "http://localhost:8085/kolicnik"

    async with ClientSession() as session:
        (status_zbroj, odgovor_zbroj), (status_umnozak, odgovor_umnozak) = await asyncio.gather(
            post_json(session, url_sum, payload),
            post_json(session, url_mul, payload),
        )

        print("Zbroj:", status_zbroj, odgovor_zbroj)
        print("Umnožak:", status_umnozak, odgovor_umnozak)

        if status_zbroj != 200 or status_umnozak != 200:
            print("Ne mogu zvati treći servis jer prvi ili drugi nisu uspjeli.")
            return

        payload3 = {"zbroj": odgovor_zbroj["zbroj"], "umnozak": odgovor_umnozak["umnozak"]}
        status_kolicnik, odgovor_kolicnik = await post_json(session, url_div, payload3)

        print("Količnik:", status_kolicnik, odgovor_kolicnik)

if __name__ == "__main__":
    asyncio.run(main())
