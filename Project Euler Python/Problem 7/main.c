/* PROBLEM 7: What is the 10001st prime number?*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int list_primes[20000] = {2};
int max_primes = 10001;
int num = 2;
int i = 0, j;

int main()
{
    while (i < max_primes)
    {
        int count = 0;
        for (j = 0; j <= i; j++)
        {
            if (num % list_primes[j] == 0)
                count++;
        }
        if (count == 0)
        {
            list_primes[i + 1] = num;
            i++;
        }
        num++;
    }
    printf("The %ith prime is %i.\n", max_primes, list_primes[max_primes - 1]);
    return 0;
}
