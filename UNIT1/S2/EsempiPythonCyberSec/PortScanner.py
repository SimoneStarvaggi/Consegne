import socket as so
#Chiediamo all'utente le informazioni
target = input ("Inserisci l'indirizzo da scansire: ")
portrange = input("Inserisci un range di porte es(5-200): ")


#Portrange si aspetta un input che sarà tra 5-1024

#di portrange prendo il primo valore, in questo caso la prima porta.
#Usando split per generare una list [porta_bassa, porta_alta] e quindi prendere la porta più bassa
lowport = int (portrange.split('-')[0])
#stessa cosa ma con la porta più alta
highport = int(portrange.split('-')[1])

print(f"Scansisco host {target} dalla porta {lowport} alla porta {highport}")
porte_chiuse = []
#Ora controlleremo porta per porta tutto le porte comprese nel range che abbiamo dato all'input iniziale.
for port in range(lowport, highport + 1):
    #apriamo una connessione
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    #usiamo connect_ex che apre e chiude la connessione e restituisce solo lo stato
    status = s.connect_ex((target,port))
    #se la connessione è riuscita darà 0
    if(status == 0):
        print(f"La porta {port} è aperta!")
    else: 
        porte_chiuse.append(port)
       #print (f"La porta {port} è chiusa!")
        s.close()   
