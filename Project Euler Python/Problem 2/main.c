/*PROBLEM 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.*/
#include <stdio.h>
#include <stdlib.h>

int num1 = 0;
int num2 = 1;
int fib = 1;
int sum = 0;

int main()
{
    while (fib < 4000000)
    {
        if (!(fib % 2))
        {
            sum = sum + fib;
        }
//        printf("%i\n",fib);
        fib = num1 + num2;
        num1 = num2;
        num2 = fib;
    }
    printf("%i\n",sum);
}
