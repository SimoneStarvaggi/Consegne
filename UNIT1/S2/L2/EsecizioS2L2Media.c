#include <stdio.h>
int main()
{
    float num1, num2, media; /* Float per inserire anche numeri decimali*/
    printf("Inserisci num1:");


    scanf("%f", &num1);


    printf("Inserisci num2");
    scanf("%f", &num2);



    media =(num1+num2) /2; /* Calcolo della media*/

    printf("La media aritmetica è: %.2f\n", media);

    return 0;




}