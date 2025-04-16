def leggiFileScelto():
    filename = input("Inserisci il nome del file da leggere: ")
    daLeggere = open(filename, "r")
    righe = daLeggere.readlines()
    daLeggere.close()
    i = 0
    somma = 0
    for riga in righe:
        somma += int(riga)
        i += 1
    somma_int = float(somma)
    media = (somma_int / i)
    print("la media è: ", media)
    
leggiFileScelto()



