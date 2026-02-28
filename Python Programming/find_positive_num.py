# Python program to print only positive number from given list


list1 = [12, -7, 5, 64, -14]

def find_positive(lst : list) -> list:
    return [ x for x in lst if x > 0]

find_positive(list1)