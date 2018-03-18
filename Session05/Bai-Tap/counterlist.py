#with count() function

# numbers = [1, 6, 8, 1, 2, 1, 5, 6]
#
# n = int(input('Enter a number? '))
# print(n, 'apppears', numbers.count(n), 'times in my list')
#
# without count() function

numbers = [1, 6, 8, 1, 2, 1, 5, 6]

n = int(input('Enter a numbers? '))
count = 0

for i in range(len(numbers)):
    if n == numbers[i]:
        count += 1

print(count)
