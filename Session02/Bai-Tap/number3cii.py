
n = int(input('Enter a number : '))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i <= 4:
            print(i * j, '  ', end='')
        else: print(i * j, ' ', end='')
    print()
