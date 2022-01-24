"""
python biltin functions

"""

# abs()

print(abs(-120))

a=10
b=13

if abs(a-b) > 2:
    print("yes")

print('----------------------------------------------------')

# all()

# search = [True, True, True,True]
search = [5, 5, 4,3]

print(all(search))

# search.append(False)
search.append(0)


print(search)
print(all(search))


print('----------------------------------------------------')

# any()

print(any(search))

print('----------------------------------------------------')

# ascii()

msg = 'Hello world ت ل ب'

print(ascii(msg))


print('----------------------------------------------------')

# bin()

print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

print('----------')
# oct()
print(oct(1))
print(oct(2))
print(oct(3))

print('----------')
# hex
print(hex(1))
print(hex(2))
print(hex(3))


print('----------------------------------------------------')

# bool()

a = 12
b= 13
print(bool(a>b))

print('----------------------------------------------------')

# breakpoint()

print('----------------------------------------------------')


print(bytearray('asd', 'utf-8'))
print(bytearray('asd', 'utf-16'))

print('----------------------------------------------------')
# callable()

c  = 12

def name():
    pass

print(callable(a))
print(callable(name))

print('----------------------------------------------------')

# chr()

for i in range(97, 120):
    print(chr(i))

print('---')

# ord()

print(ord('a'))
print(ord('b'))
print(ord('c'))


print('----------------------------------------------------')
# compile(source, filename, mode)
print('----------------------------------------------------')

# dict()

players = dict(name='p1', score=10) #{}
print(players)

# list([])

playerScore = list([10,12,13]) #[]
print(playerScore)

# set([])

age = set([12,34,67]) #{}
print(age)

# tuple([])

age_2 = tuple([12,34,67]) #(,)
print(age_2)

print('----------------------------------------------------')
# divmod(a, b)

age3 = divmod(25,5)
print(age3)

print('----------------------------------------------------')
# enumerate(iterable)

word = ['H','G','S','A','S','d','f','h']

for w in word:
    print(w)

print('----')

for i in range(len(word)):
    print(i, word[i])

print('----')

for index, value in enumerate(word):
    print(index, value)

print('----')

words = {'a':'e','f':'h','u':'k','i':45}

for i , v in enumerate(words):
    print(i, v)


print('----------------------------------------------------')

# eval()

t = '(12 ** 9) + (12** 20)'
print(t)


print(eval(t))


print('----------------------------------------------------')
# exec(object)
print('----------------------------------------------------')

# format()

print(format(255, 'x'))

print('----------------------------------------------------')

# frozenset()

frozen = [12,34,12,34,56,78]

h = frozenset(frozen) # not add options

print(h)

# h.add(3)
# print(h)


print('----------------------------------------------------')

# print(globals()) #for use in shell or not use the project

print('----------------------------------------------------')
