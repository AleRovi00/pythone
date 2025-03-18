GIORNI = ("lunedi   " +
          "martedi  " +
          "mercoledi" +
          "govedi   " +
          "venerdi  " +
          "sabato   " +
          "domenica ")

giorno = int(input("indica un giorno: "))
p = (giorno-1) * 9
print (GIORNI[p:p+9])