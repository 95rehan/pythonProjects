# Python program to find first non repeating char in a string


def find_first_non(word : str) -> str:
    freq ={}
    for chr in word:
        freq[chr] = freq.get(chr,0) +1

    for i in word:
        if freq[i] == 1:
            print(i)
            break

find_first_non("swiss")