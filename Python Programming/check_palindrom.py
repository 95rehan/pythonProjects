# Python program to check to given string is pelindrom or not



sample_word= "mom"

def check_palindrom(word : str) -> bool:
    return True if word == word[::-1] else False


check_palindrom(sample_word)