# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# #simple Function
# def greet():
#     print("Hi")
#     print("Hi")
#     print("Hi")
#
# greet()

# #Function that allows for input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# greet_with_name("Gogulan")


#Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")


#Functions with Keyword arguments
greet_with(location="london", name="gogulan")


##############Exercise 1 - Paint Area Calculator###################

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)

    print(f"You'll need {cans} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


##############Exercise 2 - Prime Number Checker###################
# Write your code below this line 👇


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


