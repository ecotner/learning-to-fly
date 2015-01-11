#include <stdio.h>

int main()
{
    char response;

    printf("+\tTurns on the laser.\n-\tTurns off the laser.\nPlease enter a response: ");
    scanf("%c", &response);
    if(response == '+'){
        printf("Laser is now ON.");
    }
    if(response == '-'){
        printf("Laser is now OFF");
    }

    getchar();
    return 0;
}
