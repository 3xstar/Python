#Пример с использованием параметров
def logger(func):
    def innerFunc(*args, **kwargs):
        print(f'Вызываем функцию {func.__name__} с аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        print(result)
        return result
    return innerFunc

#Создаем декоратор
@logger
def summ(a, b):
    return a + b

summ(5,  7)