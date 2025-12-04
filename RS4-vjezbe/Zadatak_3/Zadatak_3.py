import asyncio
import aiohttp

DOG_URL = "https://dogapi.dog/api/v2/facts"
CAT_URL = "https://catfact.ninja/fact"

async def get_dog_fact(session: aiohttp.ClientSession) -> str:
    async with session.get(DOG_URL) as response:
        response.raise_for_status()
        data = await response.json()
        return data["data"][0]["attributes"]["body"]
    
async def get_cat_fact(session: aiohttp.ClientSession) -> str:
    async with session.get(CAT_URL) as response:
        response.raise_for_status()
        data = await response.json()
        return data["fact"]
    

async def mix_facts(dog_facts: list[str], cat_facts: list[str]) -> list[str]:

    mixed: list[str] = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed.append(dog_fact)
        else:
            mixed.append(cat_fact)
    return mixed

async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [
            asyncio.create_task(get_dog_fact(session))
            for _ in range(5)
        ]

        cat_facts_tasks = [
            asyncio.create_task(get_cat_fact(session))
            for _ in range(5)
        ]

        dog_cat_facts = await asyncio.gather(
            *dog_facts_tasks,
            *cat_facts_tasks,
        )

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixed = await mix_facts(dog_facts, cat_facts)

    print("Mixane činjenice o psima i mačkama:\n")
    for fact in mixed:
        print(f"-{fact}")

if __name__ == "__main__":
    asyncio.run(main())