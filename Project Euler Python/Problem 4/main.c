/* PROBLEM 4: Find the largest palindrome made from the product of two 3-digit numbers. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse(char s[]);
void strip_newline(char s[], int size);
int test_palindrome(char s[]);
void to_string(int prod, char s[]);

char string[50];
int p_list[1000];
int i = 0;
int j;
int num1, num2, prod;

int main()
{
    for (num1 = 999; num1 > 100; num1--)
    {
        for (num2 = num1; num2 > 100; num2--)
        {
            prod = num1*num2;
            sprintf(string, "%i\0", prod);
            if (test_palindrome(string))
                {
                    p_list[i] = prod;
                    i++;
                    break;
                }

        }
    }
    printf("The largest palindrome is %i.\n", max(p_list));
    return 0;
}

void reverse(char s[])
{
    int i, j, k;
    for (i = 0, j = strlen(s) - 1; i < j; i++, j--)
    {
        k = s[i];
        s[i] = s[j];
        s[j] = k;
    }
}

void strip_newline(char s[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        if (s[i] == '\n')
        {
            s[i] = '\0';
            return;
        }
    }
}

int test_palindrome(char s[])
{
    char s2[50];
    strcpy(s2,s);
    reverse(s2);
    if (strcmp(s, s2) == 0)
        return 1;
    else return 0;
}

int max(int s[])
{
    int i;
    int max = s[0];
    int length = strlen(s);

    for (i = 0; i < length; i++)
    {
        if (s[i] > max)
            max = s[i];
    }
    return max;
}
