# Python program to find missing number in sequence

# exampl input = [1,3,4,5,6]
# output = 2
sample_input = [1,3,4,5,6]

def find_missing(lst : list)-> int:
    n = len(lst) + 1
    expected_sum = n * (n+1) //2
    actuall_sum = sum(lst)
    missing_number = expected_sum - actuall_sum
    return missing_number


find_missing(sample_input)