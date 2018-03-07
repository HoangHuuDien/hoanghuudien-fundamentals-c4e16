from turtle import *

shape("turtle")
speed(-1)

length = 5

for i in range(100):
    forward(length)
    left(90)
    length += 5

mainloop()
