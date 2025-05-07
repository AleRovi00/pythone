import datetime

class Transito:
    def __init__(self, targa, data, ora, velocita):
        self._targa = targa
        self._data = data
        self._ora = ora
        self._velocita = velocita
    #metodi getter
    def getTarga(self):
        return self._targa
    def getData(self):
        return self._data
    def getOra(self):
        return self._ora
    def getVelocita(self):
        return self._velocita
    def is_multa(self, velocitaLimite=50):
        if self._velocita > velocitaLimite * 1.03:
            return True
        else:
            return False
    
listaTransiti = []
with open("transiti_urbani.txt") as file:
    transiti = file.readlines()[1:]  # Ignora la prima riga di intestazione
    for transito in transiti:
        campi = transito.split(";")
        targa = campi[0]
        data = datetime.datetime.strptime(campi[1], "%Y-%m-%d %H:%M:%S")
        velocita = float(campi[2])
        listaTransiti.append(Transito(targa, data, None, velocita))

def targa_con_piu_transiti(listaTransiti):
    conteggio_targhe = {}
    for transito in listaTransiti:
        targa = transito.getTarga()
        if targa in conteggio_targhe:
            conteggio_targhe[targa] += 1
        else:
            conteggio_targhe[targa] = 1
    targa_max = max(conteggio_targhe, key=conteggio_targhe.get)
    return targa_max

def targa_con_piu_multe(listaTransiti):
    conteggio_multe = {}
    for transito in listaTransiti:
        targa = transito.getTarga()
        if transito.is_multa():
            if targa in conteggio_multe:
                conteggio_multe[targa] += 1
            else:
                conteggio_multe[targa] = 1
    targa_max_multe = max(conteggio_multe, key=conteggio_multe.get)
    return targa_max_multe

def multe_totali(listaTransiti):
    totale_multe = 0
    for transito in listaTransiti:
        if transito.is_multa():
            totale_multe += 1
    return totale_multe

max_transiti = targa_con_piu_transiti(listaTransiti)
print(f"La targa con più transiti è: {max_transiti}")

max_multe = targa_con_piu_multe(listaTransiti)
print(f"La targa con più multe è: {max_multe}")

tot_multe = multe_totali(listaTransiti)
print(f"Il numero totale di multe è: {tot_multe}")




    