# Очередь (Queue) позволяет передавать данные между корутинами.
# queue.put() - добавить элемент
# queue.get() - получить элемент
#queue.task_done() - убрать 1 элемент из очереди

import asyncio

async def dealer(queue, items):
    for item in items:
        await queue.put(item)
        print(f"Дилер передал: {item}")
        await asyncio.sleep(1)

async def student(queue):
    while True:
        item = await queue.get()
        print(f"Студент получил: {item}")
        queue.task_done()

async def main():
    items = ["хлеб", "молоко", "печеньки"]
    queue = asyncio.Queue() #Создание очереди
    dealer_task = asyncio.create_task(dealer(queue, items))
    student_task = asyncio.create_task(student(queue))

    await dealer_task
    await student_task
    #await queue.join() #Ожидание окончания очереди

asyncio.run(main())