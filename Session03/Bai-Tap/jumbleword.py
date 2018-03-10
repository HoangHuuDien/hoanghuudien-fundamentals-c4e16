from random import * #choice = bốc ngẫu nhiên 1 phần tử trong list ra
word = list("champion")

while True:
    shuffle(word)
    print(*word, sep=' ')
    answer = input('Your answer: ')
    if answer == 'champion':
        print('Hura')
    else: print(':( Let\'s do it again')
    break
