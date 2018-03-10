clothes = ['T-Shirt', 'Sweater']

while True:

    want = input('Welcome to our shop, what do you want (C, R, U, D)? ')

    if want == 'R':
        print('Our item: ', end='')
        print(*clothes, sep=', ')

    elif want == 'C':
        new_item = input('Enter new item: ')
        clothes.append(new_item)
        print('Our item: ', end='')
        print(*clothes, sep=', ')

    elif want == 'U':
        update_item = int(input('Update position? '))
        newitem = input('New item? ')
        clothes[update_item -1] = newitem
        print('Our item: ', end='')
        print(*clothes, sep=', ')

    elif want == 'D':
        delete_item = int(input('Delete position? '))
        remove = clothes.remove(clothes[delete_item - 1])
        print('Our item: ', end='')
        print(*clothes, sep=', ')
        break
