# Python program to check armstrong number

#  153 is armstrong number coz 1*1*1 + 5*5*5 + 3*3*3 = 153


def check_armstrong(number : int) -> bool:
    resp = sum([int(x)**len(str(number)) for x in str(number)])
    return True if resp == number else False


check_armstrong(153)


