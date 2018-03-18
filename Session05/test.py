# person = ["quy", 20, 0, "Ha Noi", "Vinh Phuc", ["coding", "manga", "ping pong"]]

# dictionary
#create
person = {
    #key : value
    "name" : "Quy",
    "age" : 20,
    "ex" : 0,
    "sex" : "male"
}

# print(person)
#
# #read
# key = "age"
# if key in person:
#     print(person[key])
# else: print('Not found')

# for k in person:    #print pairs
#     print(k, person[k])

# print(dict.values(person)) #print value hàng
#
# for value in person.values(): #cột
#     print(value)

# for key, value in person.items():
#     print(key, value)

# person['age'] = 3  #thay đổi
# print(person)

person['school'] = 'HUST'

print(person)
