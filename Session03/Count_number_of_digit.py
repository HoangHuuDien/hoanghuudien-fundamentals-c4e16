number = int(input('Enter a number'))

count = 0

game = True

while game:
    number = number // 10
    count += 1
    if number == 0:
        break

print(count)    #xử lý là xử lý, print là print
