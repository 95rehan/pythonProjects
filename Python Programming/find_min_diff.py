# Find minimum diff between element in array

sample_input = [4,6,8,2,1]

def find_min_diff(lst : list) -> int:
    min_diff = 9999*9999
    lst = sorted(lst)
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i]< min_diff:
            min_diff = lst[i+1] - lst[i]
    return min_diff

find_min_diff(sample_input)


