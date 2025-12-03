def drow_line(len = 5, direction = True, symbol = "#" ):
    for i in range(len):
        if direction == True:
            print(symbol, end="")
        else:
            print(symbol)
drow_line(10, False, "zahar")