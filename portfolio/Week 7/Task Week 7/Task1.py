from collections import Counter

#Function to return sorted list of unique letters in a string
def unique_sorted_letters(s):
    return sorted(set(s))

print("Unique sorted letters in 'cheese':", unique_sorted_letters("cheese"))