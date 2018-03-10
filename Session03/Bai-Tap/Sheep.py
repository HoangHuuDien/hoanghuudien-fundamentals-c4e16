size = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Kingsman and these are my sheep sizes')
print(*size, sep=', ')


print('Now my biggest sheep has size', max(size), 'Let\'s shear it')

size[2] = 8

print('After shearing here is my flock: ')
print(*size, sep=', ')

for i in range(len(size)):
    size[i] += 50

print('One month has passed, now here is my flock ')
print(*size, sep=', ')
