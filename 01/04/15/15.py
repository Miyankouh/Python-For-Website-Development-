# def filter_number():
#     # return [i for i in range(100) if i % 7 == 0]
#     tmp = list()
#     for i in range(100):
#         if i % 7 == 0:
#             tmp.append(i)
#     print('HelloWorld')
#     return tmp


# numbers = filter_number()
# for num in numbers:
#     print(num)

# ------------------------------------------------------------------------

# def filter_number_generator():
#     for i in range(100):
#         if i % 7 == 0:
#             yield i
#     print('hello number_generator')

# number_generator = filter_number_generator()
# for num in number_generator:
#     print(num)


# ------------------------------------------------------------------------
# list
def reader(filename):
    file = open(filename, 'r')
    data = file.read().split('\n')
    file.close()
    return data

# for row in reader('user_data.csv'):
#     print(row)


# ------------------------------------------------------------------------

def reader_generator(filename):
    for row in open(filename, 'r'):
        yield row

for row in reader('user_data.csv'):
    print(row)