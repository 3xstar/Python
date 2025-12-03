import asyncio

async def red():
    while True:
        await asyncio.sleep(1)
        print("RED")

async def green():
    while True:
        await asyncio.sleep(2)
        print("GREEN")

async def main():
    t1 = asyncio.create_task(red())
    t2 = asyncio.create_task(green())

    await t1
    await t2

asyncio.run(main())