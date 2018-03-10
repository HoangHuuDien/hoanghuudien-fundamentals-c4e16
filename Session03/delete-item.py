list = ['writing', 'speaking', 'helping']

for index, item in enumerate(list):
    print(index + 1, '. ', item, sep='')

position = int(input('Position you want to get rid of? '))

remove = list.remove(list[position - 1])

for index, item in enumerate(list):
    print(index + 1, '. ', item, sep='')
