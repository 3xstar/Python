import asyncio

async def task(url): #Создание асинхронной функции
        print(url)
        await asyncio.sleep(1)  # Свое собственное ожидание
        return url

async def main():
    result = await asyncio.gather(task("loh.com"), task("sigma.ru"), task("sanyasolo.com"))
    print(result)

asyncio.run(main())