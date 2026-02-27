# Python program to remove even numbers from list

list1 = [11, 5, 17, 18, 23, 50]


for i in list1:
    if not i % 2 :
        list1.remove(i)
        
        
print(list1)