# def greeting():
#     print("hello world")


# def info():
#     return ("boo")


# def show_name():
#     pass


# print("line 12")

# msg = greeting()

# print(msg)



print('----------------------------------------------------')


# first Positional argumant------> second  Keyword argumant
def greeting(name, age=None, *args, **kwargs):
    print(f'name: {name} \t age: {age} \t args: {args} \t kwargs: {kwargs}')


# greeting("ali", 23)         # Positional

# greeting(age=23,name='ali')  # Keyword # If we want to change the order of the arguments, we have to use the keyword

# greeting(name='ali') # defalt

# greeting('ali', 12, 13, 14, 'dfjkbn',{'kb'}) # args = (13, 14, 'dfjkbn', {'kb'})

# greeting(name='ali', age=23, re='noo')       # Keyword = (re='noo')


print('----------------------------------------------------')

from data import announce

# msg = announce('Ali', 20, [12, 11, 13, 14, 16, 18, 10, 9])
# print(msg)


def announce_student(students_list):
    for data in students_list:
        # msg = announce(data['name'], data['age'], data['scores'])
        # msg = announce(name=data['name'], age=data['age'], scores=data['scores'])
        print(announce(**data))


students = [
    {'name': 'Hosin',  'age': 18,  'scores': [12, 10, 14, 15] },
    {'name': 'Ali',    'age': 19,  'scores': [10, 14, 4, 15]  },
    {'name': 'Reza',   'age': 21,  'scores': [20, 10, 14, 12] },
    {'name': 'Amir',   'age': 20,  'scores': [12, 10, 14, 19] },
    {'name': 'Moha',   'age': 23,  'scores': [12, 10, 11, 15] },
    {'name': 'Amin',   'age': 17,  'scores': [12, 10, 11, 10] },

]

announce_student(students)


print('----------------------------------------------------')
