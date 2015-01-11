#include <stdio.h>

int main()
{
    float fahr, celcius;
    int upper, lower, step;

    lower=-40;
    upper=300;
    step=10;

    printf("Fahrenheit\tCelcius")

    for (fahr=upper; fahr>=lower; fahr=fahr-step)
    {
        celcius=(fahr-32)*(5.0/9.0);
        printf("%10.0f\t%7.2f\n", fahr, celcius);
    }

    getchar();
    return 0;
}
