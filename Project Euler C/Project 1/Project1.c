/*If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.*/

#include <stdio.h>

main(void){
    int n3=0, n5=0, n15=0, sum3=0, sum5=0, sum15=0, sum_total=0;
    while(3*n3<1000){
        sum3+=3*n3;
        n3++;
    }
    while(5*n5<1000){
        sum5+=5*n5;
        n5++;
    }
    while(15*n15<1000){
        sum15+=15*n15;
        n15++;
    }
    sum_total=sum3+sum5-sum15;
    printf("%i",sum_total);
    return 0;
}
