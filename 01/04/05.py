# Tuple in python 

names = []
list()


names = {}
names = set()


data = (1,2,3,4,5,6)
data = tuple()


#  Dictionary in Python

users = {
    "name":"ali",
    "age": 36,
    "password":1234,
}

dict(name="ali", age=23, password=1234)

print(type(users))
print('------------------------------------------------')

print(users.items())

print('------------------------------------------------')

print(users.keys())
print(users.values())

print('------------------------------------------------')

print(users['name'])
print(users['age'])
print(users['password'])

print('------------------------------------------------')

print(users.get('f', 'no key'))

print('------------------------------------------------')

print(users.pop('age'))

print(users)

print('------------------------------------------------')

print(users.setdefault('age', 20))

print(users)

print('------------------------------------------------')


new_users = {
    'full_name':'namw',
}

users.update(new_users)
print(users)

print('------------------------------------------------')

newm = {**users, **new_users}
print(newm) 

print('------------------------------------------------')

new_data = {
    (1): 'name',
    ('2', 2):'moo',
}

print(new_data)

print('------------------------------------------------')
