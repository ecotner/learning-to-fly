/* PROBLEM 3: What is the largest prime factor of the number 600851475143? */

#include <stdio.h>
#include <stdlib.h>

long long int num1 = 600851475143;
long long int num2;
long long int factor;

int main()
{
    num2 = num1;
    factor = 2;
    while (factor < num2)
    {
        if (num2 - (num2/factor)*factor == 0)
        {
            num2 = num2/factor;
        }
        factor++;
    }
    printf("The largest factor of %lld is %lld.\n",num1,num2);
    return 0;
}
