#conversion of positive int to binary

def to_binary(num):
    if num < 0:
        raise ValueError("Only positive integers are allowed.")
    return bin(num)[2:]

print(to_binary(10)) 