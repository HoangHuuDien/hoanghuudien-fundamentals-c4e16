from turtle import *

shape('turtle')
color('blue')
speed(-1)
right(135)

n = int(input('Enter square length: '))

for i in range(1, 80):
    n = n / 1.03
    forward(n)
    right(90)
    forward(n)
    right(90)
    forward(n)
    right(90)
    forward(n)
    right(100)


mainloop()
