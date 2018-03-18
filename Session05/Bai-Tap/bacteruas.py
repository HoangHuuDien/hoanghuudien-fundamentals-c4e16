bb = int(input(' How many B bacterias are there? '))

minute = int(input('how much time in minutes will we wait? '))

exponential = minute / 2

print('After', bb, 'minutes, we world have', int(2*bb**exponential), 'bacterias')
