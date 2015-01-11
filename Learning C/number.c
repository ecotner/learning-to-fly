#include <stdio.h>

int main()
{
    float num1, num2, final;

    printf("Please input 2 numbers:\n");
    scanf("%f%f", &num1, &num2);

    int op;

    printf("Please specify operation -\n(1 for addition, 2 for subtraction, 3 for multiplication, 4 for division):");
    scanf("%d", &op);

    if(op==1){
        final=num1+num2;
        printf("\nThe sum is %f.\n", final);
    }
    else if(op==2){
        final=num1-num2;
        printf("\nThe difference is %f.\n", final);
    }
    else if(op==3){
        final=num1*num2;
        printf("\nThe product is %f.\n", final);
    }
    else if(op==4){
        final=num1/num2;
        printf("\nThe quotient is %f.\n", final);
    }
    else{
        printf("\nYou fucked up, dipshit. Try again.\n");
    }
    getch();
    return(0);
}
