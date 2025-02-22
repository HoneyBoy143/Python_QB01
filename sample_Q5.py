# Write a Python program to print: 0 1 2 4 5 using a while loop and the continue keyword.

i = 0
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1