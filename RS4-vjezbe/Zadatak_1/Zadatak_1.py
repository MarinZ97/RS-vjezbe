import asyncio
import time
import aiohttp

USERS_URL = "https://jsonplaceholder.typicode.com/users"

async def fetch_users(session: aiohttp.ClientSession):
    async with session.get(USERS_URL) as response:
        response.raise_for_status()
        return await response.json()
    
async def main():
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)

    end = time.perf_counter()
    elapsed = end - start

    all_users = [user for batch in results for user in batch]

    names = [u["name"] for u in all_users]
    emails = [u["email"] for u in all_users]
    sernames = [u["username"] for u in all_users]

    print("Imena korisnika:", names)
    print("Email adrese korisnika:", emails)
    print("Username korisnika:", sernames)
    print(f"Vrijeme izvođenja: {elapsed:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())



