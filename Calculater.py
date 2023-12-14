# I am assuming that the user wants to perform calculations with 2 numbers in a calculator. 
# For more numbers, I can use a loop, but I am continuing with 2 numbers.

# Taking input for both numbers from the user
num_1 = eval(input("Enter the first number: "))
num_2 = eval(input("Enter the second number: "))

# Taking input from the user for the desired operation
opr = input("Enter the operation (+, -, *, /, % (Remainder), // (Nearest integer)): ")

# Using arithmetic operators
if opr == "+":
    print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")
elif opr == "-":
    print(f"The subtraction of {num_1} and {num_2} is {num_1 - num_2}")
elif opr == "*":
    print(f"The multiplication of {num_1} and {num_2} is {num_1 * num_2}")
elif opr == "%":
    print(f"The remainder after dividing {num_1} by {num_2} is {num_1 % num_2}")
elif opr == "//":
    print(f"The nearest integer after dividing {num_1} by {num_2} is {num_1 // num_2}")
else:
    print("Invalid Operation!!")
