import asyncio

def dealer1(items):
    for item in items:
        print(f"Дилер передал {item}")

async def student1():
    print("Студент получил товар")

async def main():
    event_loop = asyncio.get_event_loop()
    event_loop.call_soon(dealer1, ["товар1", "товар2"]) #Вызовет функцию в самое ближайшее время

    student1_event = asyncio.create_task(student1())
    await student1_event
    #await None

asyncio.run(main())