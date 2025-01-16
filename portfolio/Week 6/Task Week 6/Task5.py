# removes spaces from a message and reverse it to "encrypt" it.

def simple_encrypt(msg):
    return msg.replace(" ", "")[::-1]

print(simple_encrypt("hello world"))  