# python program to sort a dict by value

sample_input = {"a":2, "b":1}
def sort_dict(d : dict) -> dict:
    return dict(sorted(d.items(),key = lambda item:item[1]))


sort_dict(sample_input)