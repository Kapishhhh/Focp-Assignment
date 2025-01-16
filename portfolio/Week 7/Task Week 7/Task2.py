# Functions to return sorted lists of letters based on two words
def letters_in_at_least_one(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))

print("Letters in at least one of 'hello' and 'world':", letters_in_at_least_one("hello", "world"))
print("Letters in both 'hello' and 'world':", letters_in_both("hello", "world"))
print("Letters in either but not both 'hello' and 'world':", letters_in_either_but_not_both("hello", "world"))