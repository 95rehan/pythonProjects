# Python program to create fibonacci series


def fibo(n):
    a,b = 0,1
    print(a,b,end = " ")
    for i in range(n):
        c = a + b 
        a = b 
        b = c
        print(c,end= " ")

fibo(10)