# Python program to multiple all elements and get sum of a list


def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

print(multiplyList([1,2,3]))