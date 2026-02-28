# Python program to print even number in a given range


start = 4  
end = 15

def gen_even(start : int , end : int)-> list:
    return [x for x in range(start, end) if x %2 == 0]

gen_even(start, end)
        
