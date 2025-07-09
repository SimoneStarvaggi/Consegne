#Scrivere un programma in Python che genera un nome per una band musicale 
# utilizzando due input forniti dall'utente: la città di origine e il nome del proprio animale domestico.
#Richiesta di Input: Il programma deve chiedere all'utente di inserire: 
# ○ Il nome della città di origine. 
# ○ Il nome del proprio animale domestico.

#Generazione del Nome della Band: Una volta ricevuti gli input, 
#il programma deve combinare il nome della città e il nome dell'animale in un'unica stringa che rappresenta il nome della band.
#  Output: Il programma deve stampare a video il nome generato per la band.



print("Ciao! Posso aiutarti a trovare il nome per la tua band! Iniziamo...") #Messaggio iniziale della macchina


richiesta1 = input ("Qual'è la tua città di origine?") #Prima domanda per l'utente

print(richiesta1.upper())


richiesta2 = input ("Qual'è il nome del tuo animale domestico?") #Seconda domanda per l'utente

print(richiesta2.upper())

print ("Per la tua band ho pensato...") #Messaggio intermedio


band=(richiesta1 + "-" + richiesta2) #comando per la  richiesta tra primo e secondo input

print(band) #Risposta

