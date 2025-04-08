def discount(prices, isPet, nItems):
    SCONTO_APPLICATO= 0.20
    if (nItems < 6
        or nItems == 0
        or len(set(isPet)) == 1):
     return 0.00;
    i = 0
    cnt = 0
    somma= 0.0
    while i < nItems :
       if not isPet[i]:
           somma += prices[i]
           cnt += 1
       i += 1
    if cnt >= 5:
       return somma * SCONTO_APPLICATO
    else:
       return 0.00


prezzi = []
animali = []
counter = 0
utente_input = input("inserisci il prezzo: ")
while utente_input !="-1":
    prezzi.append(float(utente_input[0:utente_input.find(" ")]))
    animali.append(utente_input[-1] == "Y")
    counter += 1
    utente_input = input("inserisci il prezzo e Y/N: ")
print(discount(prezzi, animali, counter))


