import string
import argparse

from random import choices

"""
This code is better to run in Linux because access to the terminal is better

"""
def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ''

    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Password creator")
    parser.add_argument('length', type=int, help="Length of password")
    parser.add_argument(
        '-u', '--upper', help="User Upper case", action='store_true'
    )
    parser.add_argument(
        '-l', '--lower', help="User lower case", action='store_true'
    )
    parser.add_argument(
        '-d', '--digit', help="User digit case", action='store_true'
    )
    parser.add_argument(
        '-p', '--pun', help="User punc case", action='store_true'
    )

    args = parser.parse_args()
    print(create_password(
        args.length, args.upper, args.lower, args.digit, args.pun
    ))
