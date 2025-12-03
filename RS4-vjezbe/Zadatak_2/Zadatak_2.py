import asyncio
import time
import aiohttp

CATFACT_URL = "https://catfact.ninja/fact"

async def get_cat_fact(session: aiohttp.ClientSession) -> str:
    async with session.get(CATFACT_URL) as response:
        response.raise_for_status()
        data = await response.json()
        return data["fact"]
    
async def filter_cat_facts(facts: list[str]) -> list[str]:
    filtered = []
    for fact in facts:
        lower = fact.lower()
        if "cat" in lower:
            filtered.append(fact)
    return filtered

async def example():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        facts = await asyncio.gather(*tasks)

    print("\nSve dohvaćene činjenice:")
    for i, fact in enumerate(facts, start = 1):
        print(f"{i:2d}. {fact}")

    filtered = await filter_cat_facts(facts)
    print("\nFiltrirane činjenice (sadrže riječ 'cat ili cats'):")
    for i, fact in enumerate(filtered, start=1):
        print(f"{i:2d}. {fact}")

async def main():
    await example()


if __name__ == "__main__":
    asyncio.run(main())