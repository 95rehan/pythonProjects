# Python program to find cube sum of given number

"""Input : n = 5
Output : 225
13 + 23 + 33 + 43 + 53 = 225

Input : n = 7
Output : 784
13 + 23 + 33 + 43 + 53 + 
63 + 73 = 784"""

a = 7

b = 0

for i in range(a+1):
    c = i**3
    b+=c
print(b)


