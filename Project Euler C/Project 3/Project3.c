/*The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?*/

#include <stdio.h>

long long int mod(long long int x, long long int y){
    long long int z=x/y;
    return (x-z*y);
}

main(void){
    long long int num=600851475143;
    int factor=2;
    while(1){
        while(mod(num,factor)==0){
            num=num/factor;
            if(num==1){
                printf("%i\n",factor);
                exit(0);
            }
        }
        factor++;
    }
}
