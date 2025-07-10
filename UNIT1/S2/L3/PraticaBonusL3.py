#Es.1
# Scrivi una funzione che calcoli la media mobile di una lista di numeri. 
# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

lista=[1,2,3,4,5,6,7,8,9,10]
n=3
media_mobile=[]
for i in range(1,len(lista)+1):
    if i < n: 
        media=sum(lista[:i])/i
    else: 
        media=sum(lista[i-n:i])/n
    media_mobile.append(media)
print(f"La media mobile e':{media_mobile}")
