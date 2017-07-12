#include <stdio.h>

long int main(void)
{
    int n, factorial, answer;

    n=1;
    factorial=0;
    while (factorial != 'q'){
        printf("Calculate factorial of: ");
        scanf("%ld", &factorial);
        answer=1;
        for (n=1; n<=factorial; n=n+1){
            answer=answer*n;
        printf("%ld\n\n", answer);
        }
    }
    quit:
    getchar();
    return 0;
}
