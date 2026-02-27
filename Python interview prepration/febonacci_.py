# Python programm to genrate fibonacci series

# 0,1,1,2,3,5,8,13

def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a+b
        a = b
        b = c
        print(c)
        
fibo(20)