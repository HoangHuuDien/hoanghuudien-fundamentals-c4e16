h = int(input('Enter the height (cm) : '))
w = int(input('Enter the weight (kg) : '))

h = h / 100

BMI = w / (h * h)

if BMI < 16 :
    print("Severely underweight")
elif BMI > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI  < 25:
    print('Normal')
elif BMI > 25 and BMI < 30:
    print('Overweight')
else: print('Obese')
