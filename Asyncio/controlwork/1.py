import asyncio
import time

async def five_seconds():
    seconds = 0
    while seconds != 5:
        time.sleep(1)
        seconds += 1
        print(f"Прошло: {seconds} секунд")
    else:
        print("Таймер остановлен")

async def main():
    task = asyncio.create_task(five_seconds())
    await task

asyncio.run(main())