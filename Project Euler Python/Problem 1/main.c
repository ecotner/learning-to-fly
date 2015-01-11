/* PROBLEM 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000. */

#include <stdio.h>

int mult3 = 1;
int mult5 = 1;
int mult15 = 1;
int sum = 0;

int main ()
{
    while (mult3 * 3 < 1000)
    {
        sum = sum + mult3 * 3;
        mult3++;
    }
    while (mult5 * 5 < 1000)
    {
        sum = sum + mult5 * 5;
        mult5++;
    }
    while (mult15 * 15 < 1000)
    {
        sum = sum - mult15 * 15;
        mult15++;
    }

    printf("The sum is %i\n", sum);
}
