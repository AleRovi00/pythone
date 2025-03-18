MESI = ("gennaio  " +
        "febbraio " +
        "marzo    " +
        "aprile   " +
        "maggio   " +
        "giugno   " +
        "luglio   " +
        "agosto   " +
        "settembre" +
        "ottobre  " +
        "novembre " +
        "dicembre ")

mese = int(input("indica un mese: "))
p = (mese - 1) * 9
print (MESI[p] + MESI[p+1] + MESI[p+2] + MESI[p+3] + MESI[p+4] + MESI[p+5] 
       + MESI[p+6] + MESI[p+7] + MESI[p+8])
#print (MESI[p:p+9])