#include <stdio.h>

int main()
{
    int temp, digit, num, reverse = 0;
    num = 121;
    temp = num;
    while (temp != 0)
    {
        digit = temp % 10;
        reverse = reverse * 10 + digit;
        temp /= 10;
    }
    if (num == reverse)
    {
        printf("The number %d is a palindrome\n", num);
    }
    else
    {
        printf("It is not a palindrome number\n");
    }

    return 0;
}