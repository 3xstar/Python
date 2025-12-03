def repeat(n):
    def decorator(func):
        def innerFunc():
            for _ in range(n):
                func()
        return innerFunc
    return decorator

#Использование декоратора с параметрами
@repeat(3)
def message():
    print("Какое-то сообщение")

message()