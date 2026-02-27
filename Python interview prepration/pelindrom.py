# Python program to check to given string is pelindrom or not

from re import L


n = "mom"


def pelindrom(n):
    new_str = n[::-1]
    if new_str == n:
        print("Yes")
    else:
        print("NO")

pelindrom(n)