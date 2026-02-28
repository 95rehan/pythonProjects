# Python program to reveres a integer in  python

sample_input = 12345

def reverse_int(number : int) -> int:
    return int(str(number)[::-1])

reverse_int(sample_input)