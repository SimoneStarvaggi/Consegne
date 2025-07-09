Marta = 0
marta = 1  

# Non posso iniziare il con 1Marta, deve iniziare con a-zA-z o _ 

MartaPrima=1 #Questo non è un errore, ma per convenzione è usato per le classi
marta_prima=1 #Le variabili per convenzione devono essere snake_case, questo è corretto.

#Ad ogni modo le variabili sono case sensitive quindi Marta è diversa da marta
Marta=0
marta=1
print (Marta, marta)
#-----------------
#intero
x=10
#virgola mobile
y=3.14
#stringa
nome="Alice" #La stringa in fase di dichiarazione può avere diversi formati, basta anteporre
# una lettera prima delle virgolette, se metto la possibilità di inserire funzioni o variabili 
nome=f"alice {y}"
print(nome) #Risultato: Alice 3.14.

#Booleano (True/False)
utente_attivo=True
#Lista
numeri=(1,2,3,4,5)
#Tuple
coordinate = (10,20)
#dizionari
utente= {"nome": "Alice", "Eta":"25"}