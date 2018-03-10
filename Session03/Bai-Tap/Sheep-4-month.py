size = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Kingsman and these are my sheep sizes')
print(*size, sep=', ')

for i in range(1, 4):
    for j in range(len(size)):
        size[j] += 50
    print('MONTH', i)
    print('One month has passed, here is my flock')
    print(*size, sep=', ')
    print('Now my biggest sheep has size', max(size), 'Let\'s shear it')
    print('After shearing, here is my flock')
    size[size.index(max(size))] = 8
    print(*size, sep=', ')




# for i in range(len(size)):
#     size[i] += 50
# print('One month has passed, here is my flock')
# print('Now my biggest sheep has size', max(size), 'Let\'s shear it')
# print('After shearing, here is my flock')
# size[size.index(max(size))] = 8
# print(*size, sep=', ')
