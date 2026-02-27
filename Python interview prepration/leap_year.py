# Find the given year is leap year or not


from lib2to3.pytree import LeafPattern


def leap_year(year):
    if((year % 400 == 0) or(year % 100 != 0) and  (year % 4 == 0)): 
        print("Leap Year") 
    else:
        print("Not Leap Year")
        
leap_year(2001)