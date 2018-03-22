from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds117749.mlab.com:17749/hoanghuudien"

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create Collection
games = db['games']
blog = db['blog']
teencode = db['teencode']
# #4. Create a new document
# new_game = {
#     "name" : "LOL",
#     "description" : "League of Legend"
#
# }
#
# new_blog = {
#     "sky" : "blue",
#     "water" : "blue",
#     "tree" : "green"
# }
#
# new_teencode = {
#     'hc' : 'hoan canh',
#     'eny' : 'em nguoi yeu',
#     'pt' : 'phat trien',
#     'hl' : 'ham lam',
#      'ns' : 'noi',
#     }

all_game = games.find()

for game in all_game:
    print(game['name'])



# #5. Insert document into Collection
# games.insert_one(new_game)
# blog.insert_one(new_blog)
# teencode.insert_one(new_teencode)
