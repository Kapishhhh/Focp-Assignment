#finding all factors of positive integers

def find_factors(num):
    if num <= 0:
        raise ValueError("Only positive integers are allowed.")
    return [i for i in range(1, num + 1) if num % i == 0]

print(find_factors(12))  