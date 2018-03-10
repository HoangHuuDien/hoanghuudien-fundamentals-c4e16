# from random import * #choice = bốc ngẫu nhiên 1 phần tử trong list ra
# word = list("champion")
#
# while True:
#     shuffle(word)
#     print(*word, sep=' ')
#     answer = input('Your answer: ')
#     if answer == 'champion':
#         print('Hura')
#     else: print(':( Let\'s do it again')
#     break
#
#3b
from random import *
word = ["Champion", "Mission", "Attack", "Kill"]

x = choice(word)

while True:
    shuffle(list('x'))
    print(*x, sep=' ')
    guess = input('Your answer : ')
    if guess == x:
        print('Hura')
    else: print('Not true')
    break
