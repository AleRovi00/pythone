def saldo (saldo_iniziale, tasso, anni = None,):
    i = 1

    while i <= anni :
     interesse = saldo_iniziale * (tasso/100)
     saldo_iniziale += interesse
     i += 1
    print(saldo_iniziale)

saldo(10000, 4, 2)


