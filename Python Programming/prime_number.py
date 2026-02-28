# Python programm to check prime number

a = 18


if a>0:
    for i in range(2,a):
        if a % i ==0:
            print("not prime")
            break
    else:
        print("Prime")
    
        
        
    