teencode = {
    'hc' : 'hoan canh',
    'eny' : 'em nguoi yeu',
    'pt' : 'phat trien',
    'hl' : 'ham lam',
     'ns' : 'noi',
    }

while True:

    for k in teencode:
        print(k, end='    ')
    print()

    code = input('Your code? ')


    if code in teencode:
        print('Code: ', code)
        print('Translation: ', teencode[code])
    else:
         print('Not Found')
         ans = input('Do you want to contribute this word? (Y/N)? ')
         if ans == 'y':
             new = input('Enter your translation: ')
             teencode[code] = new
             print('Updated')
         else:
             break
    for k in teencode:
        print(k, end='  ')
