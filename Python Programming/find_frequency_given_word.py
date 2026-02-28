# Find frequency of a given word


sample_input = "Rehan Aaatif Khan"

def find_freq(word : str) -> dict:
    freq = {}
    for chr in word:
        freq[chr]= freq.get(chr,0) + 1
    return freq


find_freq(sample_input)