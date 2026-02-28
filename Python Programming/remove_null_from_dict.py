# python program to remove null values from a dict

sample_input = {"a":None, "b":"data"}
def remove_null(d : dict) -> dict:
    return {k:v for k,v in d.items() if v is not None}



remove_null(sample_input)