numero = input("inserisci numero: ")
somma = 0
i = 0
while numero != "exit" :
    numeroint= int(numero)
    somma += numeroint
    i += 1
    numero = input("inserisci numero: ")
    
print ("la media è: ",somma / i)

