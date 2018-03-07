from random import randint

mood = randint(0, 100)

if mood < 30 :
    print('T.T')

elif 30 < mood < 60 :
    print('.-.')
else: print('Put your hands up')
