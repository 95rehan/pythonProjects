# Python programm to check prime number

sample_number = 17


def check_primt(number : int) -> bool:
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
    return flag


check_primt(sample_number)
    
        
           