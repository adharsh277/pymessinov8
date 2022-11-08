# get keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
y = car.values()
print(x)  # before the change
print(y)
car["color"] = "white"
car['capacity'] = 8777
print(y)
print(x)  # after the change


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change


thisdict1 = {
    'brand': 'greash yeagaer',
    'model': 'eren',
    'year': 24367
}
print(thisdict1)
print(len(thisdict1))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# %35
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(thisdict["year"])
print(thisdict["brand"])
# 234
thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict2))

thisdict3 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict3)
print(type(thisdict3))
# accesing items
thisdict = {
    'brand': "ford",
    'model': 'mustang',
    'year': '1936'
}
z = thisdict['model']
y = thisdict['brand']
x = thisdict['year']
print(x)
print(y)
print(z)

# get items
bike = {
    'brand': 'bmw',
    'model': 'xx7',
    'year': '1989',
}
x = bike.items()
y = bike.keys()
z = bike.values()
print(x)
print(y)
print(z)
# yiuhvh
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x1 = car.items()

print(x1)  # before the change

car["color"] = "red"

print(x1)  # after the change
