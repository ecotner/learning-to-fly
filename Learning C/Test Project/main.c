#include <stdio.h>
#include <stdlib.h>

char string[50] = {'1','2','3','4','\0'};
int num;

int main()
{
    num = atoi(string);
    printf("%i", num);
    return 0;
}
