# Program to report the six most common letters in a string
def most_common_letters(message):
    message = message.lower()
    counter = counter(filter(str.isalpha, message))
    most_common = counter.most_common(6)
    print("The six most common letters are:")
    for letter, count in most_common:
        print(f"{letter}: {count}")

most_common_letters("This is a test message to analyze the frequency of letters.")