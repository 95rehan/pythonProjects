# Python program to find the occurrences of given element is a list

l = [15, 6, 7, 10, 12, 20, 10, 28, 10]

find = 10

count = 0

for i in l:
    if i == find:
        count+=1

print(f"the number of occurence of {find} is {count}")
