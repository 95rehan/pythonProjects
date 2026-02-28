# Python program to remove even numbers from list

sample_input = [11, 5, 17, 18, 23, 50, 2]


def remove_even(lst : list) -> list:
    return [x for x in lst if x%2 != 0]

remove_even(sample_input)