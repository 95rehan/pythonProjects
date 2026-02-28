# python program to check if element present in the list or not

example_input = [2,3,6,4,5,1,5,74]
def check_if_exists(lst : list , target : int ) -> bool:
    return True if target in lst else False


check_if_exists(example_input,5)
