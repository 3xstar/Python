import time

def timer(func):
    def inner(seconds):
        result = func()
        start_time = time.time()
        time.sleep(seconds)
        end_time = time.time()
        print(f'Функция выполнилась спустя {end_time - start_time:.3f} сек')
        return result
    return inner

@timer
def work():
    print(f"Программа начала работу...")

work(2)