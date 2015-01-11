#include <stdio.h>

int main(void)
{
    float fahr, celcius, kelvin;
    float lower, upper, step;

    printf("Temperature Conversion Chart (from Celcius)\n");

    printf("Specify lower bound: ");
    scanf("%f", &lower);
    printf("\nSpecify upper bound: ");
    scanf("%f", &upper);
    printf("\nSpecify step size: ");
    scanf("%f", &step);
    printf("Temperature Conversion Chart\n\nCelcius\tFahrenheit\tKelvin\n");

    celcius = lower;

    while(celcius <= upper) {
    fahr = (9.0/5.0) * celcius + 32;
    kelvin = celcius + 273.15;
    printf("%7.2f\t%10.2f\t%6.2f\n", celcius, fahr, kelvin);
    celcius = celcius + step;
    }
    getchar();
    getchar();
    return 0;
}
