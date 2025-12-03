a = [1, 56, 76, [2, 6, 5] ,[1 ,[1, 1], 2, 3], 6, 5]

def recursion(n):
    new_list  = []
    for i in n:
        try:
            if len(i) > 0:
                new_list.extend(recursion(i))
        except Exception:
            new_list.append(i)
    return new_list

print(recursion(a))