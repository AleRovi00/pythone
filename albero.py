lettera = input ("inserisci carattere: ")
basestr = input ("larghezza base: ")
base = int(basestr)
i = 1
while i <= base :
    print(" " * ((base-i) // 2) + lettera * (i + 1 - (base % 2)))
    i += 2
