
# C
lista = []
input_utente = input("Inserisci un numero (o 'q' per terminare): ")
while input_utente != 'q':
       lista.append(int(input_utente))
       input_utente = input("Inserisci un numero (o 'q' per terminare): ")  
       print("Il valore massimo della lista è:", max(lista))