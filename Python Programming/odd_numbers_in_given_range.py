# Python program to print odd numbers in by given range

# Python program to print even number by given a range


start = 4  
end = 15

def gen_odd(start : int , end : int)-> list:
    return [x for x in range(start, end) if x %2 != 0]

gen_odd(start, end)