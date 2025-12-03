import asyncio
import time


async def producer(queue, pizzas):
    count_pizza = 0
    while count_pizza != 3:
        for pizza in pizzas:
            time.sleep(2)
            count_pizza += 1
            await queue.put(pizza)
            print(f"Повар передал пиццу под номером: {count_pizza}")


async def consumer(queue):
    while True:
        await queue.get()
        time.sleep(1)
        print("Официант забрал пиццу со стола и доставил клиенту")
        queue.task_done()

async def main():
    pizzas = [1,2,3]
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue, pizzas))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await consumer_task

asyncio.run(main())