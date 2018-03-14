s = input('Enter a sequence of number, separated by space: ')

#strip cawst spaces at start/end of string
words = s.strip().split(' ')

numbers = []

for word in words:
    numbers.append(int(word))

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print('Your sequence is already sorted')
else: print('Your sequence is not sorted yet')

sorted_list = []

for i in range(len(numbers)):
    min_number = min(numbers)
    sorted_list.append(min_number)
    numbers.remove(min_number)

print(sorted_list)
