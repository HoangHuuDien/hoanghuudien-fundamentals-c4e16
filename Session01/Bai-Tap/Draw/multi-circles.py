from turtle import *

speed(-1)
color('green')

number = int(input("How many circles?"))

for i in range(360):
    circle(100)
    left(360 / number)

mainloop()
