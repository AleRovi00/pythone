IVA23 = 0.23
IVA35 = 0.35
IVA43 = 0.43
irpef = 0.0
scal1 = 28000
scal2 = 50000
redditostr = input("dimmi il reddito: ")
reddito = float(redditostr)
if reddito <= scal1:
    irpef = reddito * IVA23

else:
    if reddito > scal1 and reddito <= scal2:
        irpef = (scal1 * IVA23) + (reddito - scal1) * IVA35
    else:
        if reddito > scal2:
            irpef = (
                (scal1 * IVA23) + (scal2 - scal1) * IVA35 + (reddito - scal2) * IVA43
            )

print("la tua imposta è: ", irpef)
