import socket as so #Importiamo la libreria socket e tramite AS la rinominiamo
                    #come "so"
import os, subprocess
#Socket ha bisogno di una tupla contenente IP dove fare bind e porta
SRV_ADDR = "192.168.50.100"
SRV_PORT = 44444

#Creiamo un oggetto che ci faccia gestire la connessione
#S AF_INET è un iPv4, mentre SOCK_STREAM è il protocollo TCP
s=so.socket(so.AF_INET, so.SOCK_STREAM) 
#Configuriamo questo oggetto in modo da farci riservare IP e PORT
s.bind((SRV_ADDR, SRV_PORT))
#bind ha bisogno di una tupla
#Spieghiamo che deve entrare in ascolto (s.listen)
#listen(numer_connessioni_accettate)
s.listen(1)
#Ora attiviamo la connessione, ma prima avvisiamo l'utente che stiamo avviando la connessione
print("Server avviato! Sono in attesa di connessione...")
#con accept il codice si fermerà fino a che qualcuno non si collega.
#Accept ha come return una tupla (oggetto_della_connessione, ip_della_macchina_che_si_è_connessa)

#Esiste un modo più efficace su Python per fare questo:
#tc = s.accept()
#connection = tc[0]
#address = tc[1]
#Il metodo efficace si chiama destrutturazione, ovvero se ho una lista o una tupla posso dividere i valori
#su più variabili con una sintesi intuititva:
connection, address = s.accept()
print(f"Qualcuno si è connesso da: {address[0]} usando la porta {address [1]}")

#Adesso sfruttiamo connection che da adesso sta dialogando col client
while True:
    #ottengo la directory corrente
    cartella = os.getcwd()
    #facciamo un promt simile al terminale linux
    promt = f"{cartella}$"
    #lo invio al client
    connection.sendall(promt.encode())
    #mi metto in ascolto della risposta
    data = connection.recv(1024)
    #ora trasformiamo data in un comando comprensibile dal terminale di linux, quindi decode in utf8 e puliamo da \n (con strip)
    comandi = data.decode('utf-8').strip()
    #Cerchiamo il comando come "cd" "ls" ecc..
    comando = comandi[0]
    if comando == "cd":
        #la directory è il secondo argomento
        os.chdir(comandi[1])
    #possiamo ora mandare il comando al sistema
    risposta = subprocess.run(comandi.split(" "), capture_output=True, text=True)
    #Se il client non sta dialogando o ha interrotto la connessione devi uscire dal ciclo.
    if not data: break
    #se invece ha inviato dati, diamo un feedback inviando una riposta, mettiamo b prima perché le comunicazione arrivano in binario
    connection.sendall(risposta.stdout.encode())
    #stampiamo quello che il client ci ha inviato:usiamo decode così da farci decifrare i numeri binari e renderli leggibili per noi
    print(data.decode('utf-8')) #utf-8 è un tipo di codifica di caratteri, utilizzando sequenze di byte a lunghezza variabile
    #alla fine del ciclo dobbiamo chiudere la connessione
    connection.close()
