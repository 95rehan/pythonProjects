# python program to remove empty tuple from a list

sample_input = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]


def remove_empty_tups(lst : list) -> list:
    return [x for x in lst if x != ()]

print(remove_empty_tups(sample_input))