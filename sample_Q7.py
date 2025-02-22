# Write a Python program to take three numbers as input and print the greatest of those numbers using an if-else statement

# Taking three numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the greatest number using if-else statements
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Printing the greatest number
print("The greatest number is:", greatest)