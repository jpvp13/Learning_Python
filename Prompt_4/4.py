
#! 4) Determine if a number is even or odd


number = int(input("Please enter a number:"))

if (number % 2) == 0:   #~ this checks to see if the input modulo-ed returns 0, meaning even
    print("This number is even!")
elif (number % 2) == 1: #~ this checks to see if the input modulo-ed returns 1, meaning odd
    print("This number is odd!")