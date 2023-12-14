import random as rnd
import string as stri

if __name__ == "__main__":
    # Generating dictionaries for password
    s1 = stri.ascii_lowercase
    s2 = stri.ascii_uppercase
    s3 = stri.digits
    s4 = stri.punctuation

    # Making a list of all different dictionaries
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Shuffling the list using the random library
    rnd.shuffle(s)

    # Taking length of password as input
    plen = int(input("Enter the length of your password (Minimum 12 Recommended): "))

    # Generating password
    password = "".join(s[:plen])

    print(f"Your secure password is: {password}")
