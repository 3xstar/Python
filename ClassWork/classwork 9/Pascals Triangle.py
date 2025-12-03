def pascals_triangle(n):
    triangle = []
    for i in range(n):
        triangle_level = []
        for k in range(i):
            if k == 0 or k == i -1:
                triangle_level.append(1)
            else:
                triangle_level.append(triangle[i-1][k-1] + triangle[i-1][k])
        triangle.append(triangle_level)
    return triangle
print(pascals_triangle(10))
for i in pascals_triangle(10):
    print("{:^30}".format(str(i)))