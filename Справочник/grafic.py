def func(x):
    y = []
    for i in x:
        if i != 0:
            y.append(1/i)
        else:
            y.append(0)
    return y

x_list = [i/10 for i in range(-100, 101)]
print(x_list)
y_list = func(x_list)
print(y_list)

import turtle
zahar = turtle.Turtle()
zahar.shape("turtle")
zahar.color("blue")
for i in range(len(x_list)):
    zahar.setposition(x_list[i] * 10, y_list[i] * 10)
zahar.setposition(0, 0
                  )
turtle.mainloop()