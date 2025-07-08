#include <stdio.h>
/* Scrivi un programma che esegua l'operazione di moltiplicazione tra due numeri
inseriti dall'utente
Opzionale: Scrivi un programma in linguaggio C che legga due valori interi e
calcoli la media aritmetica */




int main ()
{
int num1; /*Dichiaro la veriabile del primo numero*/

int num2; /*Dichiaro la variabile del secondo numero */

int risultato; /*Dichiaro il risultato dell'operazione della prima e della seconda
variabile, in questo caso num1 e num2*/

printf("Ciao pigrone! Risolvo io i tuoi problemi chill, dammi il primo numero: ");
scanf ("%d", &num1);

printf("Devi darmi anche il secondo numero! Famo i seri:");
scanf ("%d", &num2);

risultato = num1 * num2;

printf("Il risultato è: %d\n", risultato);
printf("Sono felice di aiutarti, ma dovresti imparare a contare da solo pippone!");



return 0;


}
