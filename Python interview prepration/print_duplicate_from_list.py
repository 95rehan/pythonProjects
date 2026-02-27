# Python program to print duplicate elements from a list


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

l = set([x for x in list1 if list1.count(x) > 1])

print(l)