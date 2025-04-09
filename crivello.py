
def crea_insieme_numeri(N):
    return set(range(1, N + 1))

# Esempio di utilizzo
numeri = 20
insieme = crea_insieme_numeri(numeri)
#print(insieme)
# Rimuovere i numeri multipli da 2 a N dall'insieme
for i in range(2, int(numeri ** 1/2) + 1):
    insieme = {num for num in insieme if num % i != 0 or num == i}
print(insieme)