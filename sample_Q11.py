# Write a Python program to check whether a given number is a palindrome or not.

def main():
    num = int(input("Enter a number: "))
    temp = num
    reverse = 0

    while temp != 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if num == reverse:
        print(f"The number {num} is a palindrome")
    else:
        print("It is not a palindrome number")

if __name__ == "__main__":
    main()