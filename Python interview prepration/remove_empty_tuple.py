# python program to remove empty tuple from a list

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]

for i in tuples:
    if i == ():
        tuples.remove(i)

print(tuples)