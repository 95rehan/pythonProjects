# Find longest word in sentence


sample_input = "Rehan aatif khan from ramgarh"

def find_longest_word(sentence : str) -> str:
    return max(sentence.split(), key = len)


find_longest_word(sample_input)