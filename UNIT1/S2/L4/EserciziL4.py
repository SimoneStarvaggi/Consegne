#Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche 
#(scegliete pure quelle che volete voi). Per la risoluzione dellʼesercizio abbiamo scelto:
import math
#def perimetro() 



print("Ciao, io calcolo il perimetro di diverse figure geometriche")
print(""" 
      cerchio = a
      Quadrato = b
      Rettangolo = c""")
scelta=input("scegli: ")
if  scelta == "a":
    raggio=float(input("Dimmi il raggio da calcolare: "))
    circonferenza=raggio*2*math.pi
    print(f"La formula per calcolare il perimetro del cerchio è {round(circonferenza,2)}.")
elif scelta == "b":
    lato=float(input("Dammi uno dei lati del quadrato e ti calcolerò il suo perimetro: " ))
    perimetro=lato*4
    print (f"Il perimetro del tuo quadrato è {round(perimetro)}.")
elif scelta == "c":
     base=float(input("Dimmi la base del rettangolo"))
     altezza=float(input("Dimmi l'altezza del rettangolo"))
     perimetrorett=(altezza*2 + base*2)
     print(f"Il perimetro del rettangolo è {round(perimetrorett)}")
   
else: ("Non so risponderti")





