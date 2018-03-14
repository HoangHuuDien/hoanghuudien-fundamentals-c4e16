from random import randint
print('Guess your number game')

think = input("Now think of a number from 0 to 100, then press 'Enter' ")

print(""" All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number""")
low = 0
high = 101

while True:
    mid = (low + high) // 2
    ans = input("Is {0} your number?".format(mid)).lower()           #hoặc dùng upper => ra chữ hoa
    if ans == 'c':
        print('I knew it')
        break
    elif ans == 'l':
        high = mid
    elif ans == 's':
        low = mid
    else: print('Ezzz')


#string formatting input("Is {0} your number?.format(50)") hoặc thiếu gì đẩy cái đó vào theo đúng thứ tự "{0} has {1} ex-gf".format('King', 50)
# answer = input('Is {0} your number?'.format(guess))
#
# while True:
#     if answer == 's':
#         high = high / 2
#         answer = input('Is {0} your number?'.format(high))
#     if answer == 'l':
#         guess = guess / 2 #trong format chỉ format biến hoặc số, không format được biểu thức
#         answer = input('Is {0} yout number?'.format(guess))
#     if answer == 'c':
#         print('I knew it')
#         break
