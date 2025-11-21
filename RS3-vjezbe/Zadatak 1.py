import asyncio
import time

async def fetch_numbers():
    await asyncio.sleep(3) 
    numbers = [x for x in range(1,11)]
    print("Podaci su dohvaćeni")
    return numbers

async def main_task():
    start = time.perf_counter()
    result = await fetch_numbers()
    duration = time.perf_counter() - start
    print(f"Rezultat: {result}")
    print(f"Vrijeme izvršavanja: {duration:.2f} s\n")

asyncio.run(main_task())