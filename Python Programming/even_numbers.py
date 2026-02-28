# Python program to find even numbers from a list

sample_input = [2,3,4,5,6,7,8,9,10]

def find_even(lst : list) -> list:
    return [x for x in lst if x % 2 == 0]


find_even(sample_input)

