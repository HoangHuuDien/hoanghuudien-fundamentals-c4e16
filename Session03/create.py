love = ['chuối', 'bưởi', 'nhãn', 'cần sa'] # 0 1 2 3 

print('Hello, here is the thing you love')
print(*love, sep=', ')

n = input('Write more')
love.append(n)

print(*love, sep=', ') #seperator
