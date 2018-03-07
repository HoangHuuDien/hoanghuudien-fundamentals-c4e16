from turtle import *

shape('turtle')
speed(-1)
color('black')

number = int(input("So Canh Cua Da Giac La:"))
begin_fill()
for i in range(number):

    forward(100)
    left(360 / number)
end_fill()
mainloop()
