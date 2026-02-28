# Python program to check given number is armstrong or not


def armstrong(n):
    new = [int(x)**3 for x in str(n)]
    total = sum(new)
    if n == total:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
armstrong(153)
    
    
