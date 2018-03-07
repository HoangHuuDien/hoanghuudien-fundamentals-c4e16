yob = int(input("Your year of birth"))

age = 2018 - yob

print("Your age: ", age)

if age < 10 :
    print('Baby')

elif age <= 18 :
    print('teenager')

elif age == 24 :
    print('Chet me may')

else:
    print('Not baby')

print('Bye')
