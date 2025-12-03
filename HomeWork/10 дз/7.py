def palindrom_list(help="Введите шестизначное число для определения палиндрома: "):
    while True:
        a = input(help)
        if len(a) == 6:
            a = int(a)
            return(a)
        else:
            print("Вы не шестизначное число, попробуйте снова")
def palindrom_func(a):
    a = str(a)
    if len(a) == 6:
        start = a[0] + a[1] + a[2]
        end = a[5] + a[4] + a[3]
        if start == end:
            print("True")
        else:
            print("False")
a = palindrom_list()
palindrom_func(a)
