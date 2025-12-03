import asyncio

async def ping():
    ping_count = 0
    while True:
        await asyncio.sleep(1)
        ping_count += 1
        print("Пинг")

async def pong():
    pong_count = 0
    while True:
        await asyncio.sleep(2)
        pong_count += 1
        print("Понг")

ping_pong = [asyncio.ensure_future(ping()),
                asyncio.ensure_future(pong())]

ping_pong_loop = asyncio.get_event_loop()

ping_pong_loop.run_until_complete(asyncio.gather(*ping_pong))
