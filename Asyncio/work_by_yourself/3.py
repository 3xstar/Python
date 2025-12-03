import asyncio

async def check_stop():
    while True:
        user_input = await asyncio.to_thread(input, "Введите 'stop' для выхода: ")
        if user_input.strip().lower() == "stop":
            print("Завершение работы...")
            exit()

async def print_status():
    while True:
        print("Программа работает...")
        await asyncio.sleep(10)

async def main():
    task1 = asyncio.create_task(print_status())
    task2 = asyncio.create_task(check_stop())
    await asyncio.gather(task1, task2)

asyncio.run(main())