number = int(input('Nhap so: '))

is_prime = True

# for i in range(2, number):    # có thể chỉ cần xét từ 2 ---> căn n vì nếu chia hết trong khoảng đó thì sẽ có kết quả từ căn n ---> n
#     if number % i == 0:
#         is_prime = False
#         break
#
# if is_prime == True:    # có thể bỏ qua == True
#     print(number, 'is a prime number')
# else: print(number, 'is not a prime number')
i = 2

while i <= (number ** 0.5): # có thể chỉ cần xét từ 2 ---> căn n vì nếu chia hết trong khoảng đó thì sẽ có kết quả từ căn n ---> n
    if number % i == 0:
        is_prime = False
        break

    i += 1

if is_prime == True:    # có thể bỏ qua == True
    print(number, 'is a prime number')
else: print(number, 'is not a prime number')
