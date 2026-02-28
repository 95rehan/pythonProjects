# Python programm to genrate fibonacci series

# 0,1,1,2,3,5,8,13

def gen_fibo(target : int):
    a ,b = 0, 1
    for i in range(target):
        print(a , end= " ")
        a, b = b , a + b

gen_fibo(10)