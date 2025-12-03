def sum(n, a = 1, b = 1):
    print(a + b)
    a, b = b, a+b
    n -= 1
    if n == 0:
        return None
    sum(n, a, b)
sum(10)