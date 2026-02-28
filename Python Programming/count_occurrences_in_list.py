# Python program to find the occurrences of given element is a list

example_input = [15, 6, 7, 10, 12, 20, 10, 28, 10]


def find_occr(lst : list, target : int)-> int:
    return lst.count(target)


find_occr(example_input, 10)


# other way but not recomended


def find_oc(lst : list, target : int)-> int:
    count = 0
    for i in lst:
        if i == target:
            count+=1
    return count


find_oc(example_input, 10)