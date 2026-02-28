# pyhton program to check if given string have balanced parantheses

sample_input = "{([])}"
def check_balance(st : str) -> bool:
    pairs = {"}":"{",
              "]":"[",
             ")":"("}
    
    stack = []

    for i in st:
        if i in "{([":
            stack.append(i)
        elif i in "})]":
            if not stack or stack.pop() != pairs[i]:
                return False
            
    return not stack

check_balance(sample_input)