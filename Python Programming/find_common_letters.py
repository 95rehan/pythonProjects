# Find common letters from two words


first_word = "NAINA"
second_word = "REENA"

def common_letters(first_word : str, second_wrod : str) -> str:
    return set(first_word) & set(second_wrod)

common_letters(first_word, second_word)