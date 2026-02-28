# Python program to check armstrong number

#  153 is armstrong number coz 1*1*1 + 5*5*5 + 3*3*3 = 153


def arm_strong(n):

    b = [x for x in str(n)]

    c =sum([ int(y)**3 for y in b])

    if n == c:
        print("armstrong")
    else:
        print("Not armstrong")
 
arm_strong(154)   



