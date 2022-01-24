#  List

age = 19
name = 'majid'
weight = 98.98

record = [15, 16, 12, 14, 20, 11]
# records = list() = []

print(record)
print(record)
print(record)
print(record)
print(record)
print(record)

print('---------------------------------------------------------')

print(len(record)) # 6

print(record[len(record)-1]) # last num > 11

print(record[-1]) # last num > 11

print('---------------------------------------------------------')


print(record[0]) # 15
print(record[1]) # 16 
print(record[2]) # 12
print(record[3]) # 14
print(record[4]) # 20
print(record[5]) # 11

print('---------------------------------------------------------')


# Add item to the list

record.append(17)
print(record)

record[0] = 13.45
print(record)

print('---------------------------------------------------------')

print(type(record))

record.append(name)
print(record)

print(type(record)) # list

print(type(record[-1])) # str


records_1 = [1,2,3,4,5,6]

records_2 = [1,2,3,45,6,7,8,9]

allrecords = [records_1, records_2]
print(allrecords)
print(type(allrecords[0])) # list > records_1
print(type(allrecords[1])) # list > records_2

print(len(allrecords[1])) # 8 > records_2 


print('---------------------------------------------------------')

# Retrieve data form list

# record = [<index-number>]
# record.pop()
# record.pop(<index-number>)


print(record)

record.pop()   
print(record)

record.pop()
print(record)

record.pop(-3)
print(record)

print('-------------------------------')

list_1 = [1,2,3,45,6,7,8,9]

# list slicing

print(list_1[0:3]) # [1,2,3]
print(list_1[4:6]) # [6,7]
print(list_1[1:7]) # [2,3,45,6,7,8] 
print(list_1[-3:]) # [7,8,9]

print('--')

print(list_1[::3]) # [1,45,8]
print(list_1[4::3]) # [6,9]
print(list_1[1:7:3]) # [2,6]
print(list_1[2::3]) # [3,7]


print('-------------------------------')

# extend

list_2 = [1,2,3]
list_3 = [4,5,6]

list_2.extend(list_3)
print(list_2)

print('-------------------------------')

# count

list_4 = ['fo','ali','name','name','fo', 'name','fo','name']

print(list_4.count('fo')) 

print(list_4.count('name')) 

print('-------------------------------')

# insert

list_5 = ['mo','to','so','name','dy',]
list_5.insert(2, 'king')
print(list_5)

print('-------------------------------')

# remove

list_6 = ['mo','to','so','name','dy']
list_6.remove('so')
print(list_6)


print('-------------------------------')

# reverse

list_6.reverse()
print(list_6)

print('-------------------------------')

# sort

list_7 = [9,8,7,6,5,4,3,2,1]
list_8 = [1,4,6,8,5,9,7,3,2]

list_7.sort()
print(list_7)

list_8.sort()
print(list_8)