like = ['black panther', 'captain america', 'dr strange']

for index, item in enumerate(like):
    print(index + 1, '. ', item, sep='')


n = int(input('Another hero you like more? '))
new = input('Which hero? ')
like[n-1] = new

for index, item in enumerate(like):
    print(index + 1, '. ', item, sep='')
