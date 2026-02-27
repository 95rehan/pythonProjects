# Python program to reveres a integer in  python


a  = 123456


b = [x for x in str(a)]
c = int("".join(b[::-1]))

print(c)