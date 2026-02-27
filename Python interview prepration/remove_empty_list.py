# Python program to remove empty list from a list

test_list = [5, 6, [5], 3, [], 9]


for i in test_list:
    if i == []:
        test_list.remove(i)

print(test_list)

