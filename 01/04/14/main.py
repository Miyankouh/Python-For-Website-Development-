from utils import nest2
# user = input('Enter your age: ')

# try: 
#     user_age = int(user)
#     user_data = open('user_data.csv', 'w')
# except ValueError:
#     print('invalid age')
# except NameError :
#     print('Invalid varible')
# else:
#     print('well done')
# finally:
#     print('Process finished')
#     user_data.close()


#---------------------------------------------------------

def nest():
    print('hello from nest1')
    nest2()
    print('bye from nest1')
try:
    nest()
except ValueError:
    print('value error raised')