#  If 

# age = 15

# if age > 20:
#     # start of if body
#     print("your age is more then 20")
#     print("simple text")
#     # end of if body
# elif age <= 20:
#     print("your age is  less than 20")

# elif age <= 15:
#     print("your age is  less than 20 your age 15")

# else:
#     print("your age is less 10")


# print('---------------')

number = int(input("Enter number: "))


if number == 0 :
    print('Number is 0')

elif number % 2  == 0 and number % 3 == 0:
    print('Number is divisible by 2 and 3')

elif number % 7 ==0 or number % 3 ==0:
    print('Number is divisible by 7')

else:
    print('Number is not divisible')



print('---------------')

# input alowers string

# name = input("Enter your name: ")
# q = input("Enter your age: ")

# print(f"hello {name}")
# print(f"your age {q}"   ,f"type: {type(q)}")