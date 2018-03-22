from pymongo import MongoClient
import matplotlib
matplotlib.use('tkAgg')
from matplotlib import pyplot
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database

customers = db["customers"]

n = customers.find()

ads = 0
wom = 0
events = 0

for ref in n:
    if ref['ref'] == 'ads':
        ads += 1
    elif ref['ref'] == wom:
        wom += 1
    else: events += 1

print("Number of customers group by refs")
print("wom: {}, ads: {}, events: {}".format(wom, ads, events))

labels = ["wom ","ads","events"]
values = [wom, ads, events]
colors = ["red","blue","black"]

pyplot.pie(values, labels = labels, colors = colors, explode = explode)
pyplot.axis("equal")

pyplot.show()
