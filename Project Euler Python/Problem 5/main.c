/* PROBLEM 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */

#include <stdio.h>
#include <stdlib.h>

int num = 10, sum, i;

int main()
{
    while (1)
    {
        sum = 0;
        for (i = 2; i < 20; i++)
        {
            sum = sum + (num % i);
        }
        if (sum == 0)
            {
                printf("The smallest number divisible by 1 thru 20 is %i.\n", num);
                break;
            }
        else num++;
    }

    return 0;
}
