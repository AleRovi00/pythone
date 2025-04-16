def leggiFileScelto():
    filename = input("Inserisci il nome del file da leggere: ")
    daLeggere = open(filename, "r")
    righe = daLeggere.readlines()
    daLeggere.close()
    i = 0
    somma = 0
    lista=[]

    for riga in righe:
        somma += float(riga)
        i += 1
    media = (somma / i)
    if i == 0:
        print("La somma è zero")
    print("la media è: ", media)

    for riga in righe:
        lista.append(float(riga))
    if lista:
        print("Il valore massimo della lista è:", max(lista))
        
    
leggiFileScelto()



