from time import time
import random

# Function to calculate typing speed in words per minute (WPM)
def speedtime(time_s, time_e, user_input):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    
    # Assuming an average word length of 5 characters
    speed = (len(user_input) / 5) / (time_r / 60)
    return round(speed)

# Function to count the number of mistakes in the user's input
def mistakes(partest, user_input):
    error = 0
    min_length = min(len(partest), len(user_input))
    
    for i in range(min_length):
        if partest[i] != user_input[i]:
            error += 1

    # Add the absolute difference in lengths to the error count
    error += abs(len(partest) - len(user_input))

    return error


# loop for the typing speed test
while True:
    chk = input("Do you want to continue (yes or no)? :- ")
    
    if chk.lower() == "yes":
        passages = [
            "Typing speed tests are quick assessments designed to measure how fast and accurately an individual can type on a keyboard. These tests are commonly used by employers to evaluate candidates for roles that involve substantial computer usage, ensuring that potential hires can efficiently handle tasks such as data entry and document creation. Additionally, typing speed tests have become popular tools for self-assessment and personal development, allowing individuals to track their progress and identify areas for improvement.",
            "Conducting a typing speed test typically involves presenting the test-taker with a passage or set of words to be typed within a specified time limit. The results are often measured in words per minute (WPM), taking into account both speed and accuracy. With the prevalence of online platforms, individuals can easily access free typing speed tests to practice and refine their keyboarding skills. These tests may vary in complexity, catering to different needs, such as specialized tests for programmers or professionals in specific fields.",
            "Beyond its significance in professional settings, improving typing speed offers practical benefits for everyday tasks. Increased typing proficiency contributes to enhanced productivity, enabling individuals to navigate digital environments more swiftly. Numerous resources, ranging from interactive software to online tutorials, are available for those looking to boost their typing skills. Whether pursuing career opportunities or aiming for personal growth, regular engagement with typing speed tests proves to be a valuable and accessible means of refining one's digital literacy in today's tech-driven world."
        ]
        
        random.shuffle(passages)
        ptest = passages[0:1]
        print()
        print()
        print()
        t1 = time()
        print(ptest)
        user_input = input("Enter: ")
        t2 = time()
        print(f"Your typing speed is: {speedtime(t1, t2, user_input)} WPM")
        print(f"and errors are: {mistakes(ptest, user_input)}")
        
    elif chk.lower() == "no":
        print("Thank you")
        break
    else:
        print("Wrong input!!")
