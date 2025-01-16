def greating():
    a=input("What's Your Name? : ")
    if a!="":
        print(f'Hello {a}')
    else:
        print(f'Well, Hello Stranger')
    return a

def passkey(a):

    while True:
        BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

        pword=input(f"Enter Password {a} : ")
        pword_len=len(pword)

        if pword_len < 8:
            print("Password must be over 8 more character long!")
            continue
        elif pword in BAD_PASSWORDS:
            print(f"Password cannot be {BAD_PASSWORDS}")
            continue
        else:
            pword2=input(f"Enter Password Aganin {a} : ")
            if pword == pword2:
                print("Password Set Sucessfully!")
                break
            else:
                print ("Dissimilar or Invalid Password!")

if __name__ == "__main__":
    name=greating()
    passkey(name)