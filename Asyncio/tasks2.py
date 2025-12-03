import asyncio

async def task_one(): #Создание асинхронной функции
    while True:
        await asyncio.sleep(1) #Свое собственное ожидание
        print("task1")

async def task_two():
    while True:
        await asyncio.sleep(2)
        print("task2")

tasks = [
    asyncio.ensure_future(task_one()),
    asyncio.ensure_future(task_two())
] #Список функций, которые запустятся в будущем

event_loop = asyncio.get_event_loop() #Получить цикл асинхронности
event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()