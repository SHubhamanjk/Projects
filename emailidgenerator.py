import random
import string

# Generate lowercase letters, uppercase letters, and digits
str1 = string.ascii_lowercase
str2 = string.ascii_uppercase
str3 = string.digits

# Convert digits to a list for shuffling
dic1 = list(str3)

# Create an empty list for the final character set of the email
dic = []
dic.extend(str1)
dic.extend(str2)

# Add "@" and "gmail.com" to the character set
imp = list("@gmail.com")

# Shuffle the character sets for randomness
random.shuffle(dic)
random.shuffle(dic1)

# Function to generate email
def emailgenerator():
    # Ask user if they want to add their name in the email
    nameconfirm = input("Do you want to add your name in your email id (yes or no):- ")

    if nameconfirm.lower() == "no":
        # If no, ask for the number of letters and digits in the email
        let = int(input("Enter the number of letters in your email (excluding @gmail.com) (min 6 recommended):- "))
        dig = int(input("Enter the number of digits in your email id (min 3 recommended):- "))
        # Create the email by combining letters, digits, and "@" and "gmail.com"
        email = dic[0:let] + dic1[0:dig] + imp
        finalemail = "".join(email)
        print(f"Your email id is :- {finalemail}")
        again()  # Ask user if they want to generate another email

    elif nameconfirm.lower() == "yes":
        # If yes, ask for the name, number of letters, and digits in the email
        name = input("Enter your name :- ")
        let = int(input("Enter the number of letters in your email (excluding name and @gmail.com) (min 3 recommended):- "))
        dig = int(input("Enter the number of digits in your email id (min 3 recommended):- "))
        # Create the email by combining name, letters, digits, "@" and "gmail.com"
        email = list(name) + dic[0:let] + dic1[0:dig] + imp
        finalemail = "".join(email)
        print(f"Your email id is :- {finalemail}")
        again()  # Ask user if they want to generate another email

    else:
        print("Invalid input")

# Function to ask if the user wants to generate another email
def again():
    while True:
        confirm = input("Do you want to generate the email again (yes or no) :- ")
        if confirm.lower() == "yes":
            emailgenerator()
        elif confirm.lower() == "no":
            print("Thank you")
            break
        else:
            print("Invalid input")

# Initial call to start the email generation process
emailgenerator()
