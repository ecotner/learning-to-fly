/* PROBLEM 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.*/

#include <stdio.h>
#include <stdlib.h>

#define sqr(x) x*x

int sum_sqr = 0;
int sqr_sum = 0;
int num = 100;
int i;

int main()
{
    for (i = 1; i <= num; i++)
    {
        sum_sqr = sum_sqr + sqr(i);
    }
    for (i = 1; i <= num; i++)
    {
        sqr_sum = sqr_sum + i;
    }
    sqr_sum = sqr(sqr_sum);
    printf("sum of squares: %i; square of sum: %i\n", sum_sqr, sqr_sum);
    printf("The difference between the square of the sum and the sum of the squares of the first %i natural numbers is %i.\n", num, sqr_sum - sum_sqr);
    return 0;
}
