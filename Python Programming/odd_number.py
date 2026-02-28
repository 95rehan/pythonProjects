# Python program to print odd number from a given list


sample_input = [2,3,4,5,6,7,8,9,10]

def find_odd(lst : list) -> list:
    return [x for x in lst if x %2  != 0]

print(find_odd(sample_input))