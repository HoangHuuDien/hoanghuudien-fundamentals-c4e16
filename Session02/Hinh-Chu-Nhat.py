# width = int(input('Enter width :'))
# height = int(input('Enter height :'))
#
# for i in range(width) :
#     print('*' * height)

# for i in range(3) :
#     for j in range(4):
#         print('*', end='')
#
#     print()

for i in range(6): #cai nay la de xuong dong ne
    for j in range(6):
        if j >= 6 - i:
            print('*', end='')
        else:
            print(' ', end='')

    print() #cai nay la de xuong dong sau moi lan print
