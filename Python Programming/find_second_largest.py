# Python program to find second largest number in a list


sample_input = [5,6,4,8,9,10,8,11]

def second_max(lst : list) -> int:
    return sorted(list(set(lst)))[-2]


second_max(sample_input)

