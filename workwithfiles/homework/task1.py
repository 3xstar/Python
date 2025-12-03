with open('task1.txt') as f:
    count = sum(1 for _ in f)

print(count)