def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# it is looping through the numbers from 1 to 19
# 2. When is the function meant to print "You got it"?
# when i is equal to 20
# 3. What are your assumptions about the value of i?
# i will never be 20 because the range is only from 1 to 19

# This is how it should be

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()