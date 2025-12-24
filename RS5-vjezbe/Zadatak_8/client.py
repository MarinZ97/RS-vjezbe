import asyncio
from aiohttp import ClientSession

async def main():
    amount = 15

    url_get = f"http://localhost:8086/cat?amount={amount}"
    url_post = "http://localhost:8087/facts"

    async with ClientSession() as session:
        async with session.get(url_get) as r1:
            data1 = await r1.json()
            facts = data1.get("facts", [])
            print("Dohvaćeno:", len(facts))

        async with session.post(url_post, json={"facts": facts}) as r2:
            data2 = await r2.json()
            filtered = data2.get("facts", [])
            print("Nakon filtera:", len(filtered))

            for f in filtered[:5]:
                print("-", f)

if __name__ == "__main__":
    asyncio.run(main())