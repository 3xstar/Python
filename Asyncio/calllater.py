import asyncio

def dealer1(items):
    for item in items:
        print(f"Дилер передал {item}")

async def student1(event_loop):
    time = event_loop.time() #Получить текущее время
    print(time)
    event_loop.call_at(time + 2, dealer1, ["товар3", "товар4"]) #Вызов функции в конкретное время

    print("Студент получил товар")
    await asyncio.sleep(3)

async def main():
    event_loop = asyncio.get_event_loop()
    event_loop.call_later(2, dealer1, ["товар1", "товар2"]) #Вызовет функцию через какое-то время

    student1_event = asyncio.create_task(student1(event_loop))
    await student1_event
    #await None

asyncio.run(main())