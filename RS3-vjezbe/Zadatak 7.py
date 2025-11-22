import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
    await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
    asyncio.create_task(timer('Timer 1', 3)), # Kreiramo 3 taska u main() - Timer 1, 2 i 3
    asyncio.create_task(timer('Timer 2', 5)),
    asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers) # gather pokreće sve taskove istovremeno

# Event loop raspoređuje korutine tako da se izvršavaju bez blokiranja. Svaki timer je zaseban task i počinje se izvršavat odmah
# Korutina kada dođe do "await" onda se pauzira i prebacuje na drugi task
# gather pričeka sve taskove da završe, program završava kada istekne najduži timer (Timer 3)

asyncio.run(main()) # Kreiramo i pokrećemo event loop 