# Python program to check the greatest int 


n = 123

def greatest(n):
    new_list = [int(x) for x in str(n)]
    new_list.sort()
    

    return(new_list[-1])     


print(greatest(n))       
    