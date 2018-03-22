import matplotlib

matplotlib.use('TkAgg')

from matplotlib import pyplot

#1. Prepare data

labels = ['Web', 'iOS', 'Android', 'React Native']

values = [40, 20, 25, 15]

colors =['red', 'green', 'gold', 'purple']

explode = [0, 0.2, 0.4, 0.5] #cut



#2. pyplot

pyplot.pie(values, labels = labels, colors = colors, explode = explode)
pyplot.axis('equal')

#3. Show
pyplot.show()
