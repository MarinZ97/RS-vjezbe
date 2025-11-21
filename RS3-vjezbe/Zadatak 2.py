import asyncio
import time

async def fetch_users():
    await asyncio.sleep(3)
    users = ["Petar", "Mirko", "Marko", "Mujo"]
    print("Podaci o korisnicima su dohvaćeni")
    return users

async def fetch_products():
    await asyncio.sleep(5)
    products = ["Laptop", "Monitor", "Tipkovnica", "Miš"]
    print("Podaci o proizvodima su dohvaćeni")
    return products

async def main_task():
    start = time.perf_counter()
    users, products = await asyncio.gather(fetch_users(), fetch_products())
    duration = time.perf_counter() - start
    print(f"Korisnici: {users}")
    print(f"Proizvodi: {products}")
    print(f"Vrijeme izvršavanja: {duration:.2f} s\n")

asyncio.run(main_task())
