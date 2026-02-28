# Python program to create sum to two element from a list


"""Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]"""

l = [10, 20, 30, 40, 50]

b = []
c = 0

for i in l:
    c+= i
    b.append(c)

print(b)

        


