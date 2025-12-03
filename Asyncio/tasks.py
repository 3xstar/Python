import asyncio

async def task_one(): #создание асинхронной функции
    while True:
        await asyncio.sleep(1) #свое собственное ожидание
        print("task1")

async def task_two():
    while True:
        await asyncio.sleep(2)
        print("task2")

async def main():
    t1 = asyncio.create_task(task_one()) #создание таска
    t2 = asyncio.create_task(task_two())

    await t1
    await t2

asyncio.run(main())