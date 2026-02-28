# Python program to print duplicate elements from a list


sample_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

def find_dups(lst : list) -> list:

    return list(set([x for x in lst if lst.count(x) > 1]))

print(find_dups(sample_list))