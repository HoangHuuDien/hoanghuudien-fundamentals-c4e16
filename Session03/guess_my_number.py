from random import randint

# my_number = randint(0, 100)

my_number = 99


playing = True #biến này là để close vòng lặp thui mà :">4

count = 0

while playing:
    n = int(input('Thu doan xem nao ? '))
    if n < my_number:
        print('It is smaller than normal')
    elif n > my_number:
        print('It is too big baby')
    else:
        print('True Baby')
        break            #nghỉ luôn, phá vòng lặp, về quê
    count += 1
    if count == 7:
        print('You lose :(')
        break
