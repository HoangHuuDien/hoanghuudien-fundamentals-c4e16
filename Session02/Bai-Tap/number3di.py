for i in range(1, 10):
    for j in range(1, 10):
        if i % 2 == 0 and j % 2 != 0:
            print(' 1 ', end='')
        elif i % 2 != 0 and j % 2 == 0:
            print(' 1 ', end='')

        else: print(' 0 ', end='')

    print()
