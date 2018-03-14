name = input('Enter your name: ')

words = name.split()

for i in range(len(words)):
    words[i] = words[i].title()
print(' '.join(words))
