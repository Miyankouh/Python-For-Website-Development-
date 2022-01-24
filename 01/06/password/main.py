import string

from random import choices


def create_password(length=12, upper=False, lower=False, digits=False, pun=False):
    pool = ''

    if upper:
        pool += string.ascii_uppercase 

    if lower:
        pool += string.ascii_lowercase

    if digits:
        pool += string.digits

    if pun:
        pool += string.punctuation
 
    if pool == '':
        pool += string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == '__main__':
    print(create_password())

    # print(create_password(length))
    # print(create_password(upper=True,))
    # print(create_password(lower=True,))
    # print(create_password(upper=True, digits=True, ))
    # print(create_password(lower=True, digits=True, pun=True))
    # print(create_password(lower=True, digits=True, pun=False))