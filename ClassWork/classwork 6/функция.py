width, length, height = 10, 15, 10
width1, length1 = 10, 15
def area(a, b):
    area = a * b
    print(f"Площадь помещения: {area}")
    return area
def perimetr(a, b):
    print(f"Периметр помещения: {(a + b) * 2}")
def volume(s, h):
    print(f"Объем помещения: {s * h}")

# s = area(width, length)
# perimetr(width, length)
# # volume(s, height)
# volume(area(width,length), height)
print(f"Параметры помещения: {perimetr(width, length)} {volume(area(width,length), height)} ")