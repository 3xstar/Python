import asyncio

async def every_second():
    seconds = 0
    while True:
        await asyncio.sleep(1)
        seconds += 1
        print("Прошло секунд: ", seconds)

async def every_minute():
    minutes = 0
    while True:
        await asyncio.sleep(60)
        minutes += 1
        print("Прошло минут: ", minutes)

async def main():
    s = asyncio.create_task(every_second())  # создание таска
    m = asyncio.create_task(every_minute())

    await s
    await m

asyncio.run(main())
