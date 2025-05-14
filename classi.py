class Persona:
    def __init__(self, nome, anno_nascita):
        self._nome = nome
        self._anno_nascita = anno_nascita

    def __repr__(self):
        return f"Nome: {self._nome}, Anno di nascita: {self._anno_nascita}"

class Studente(Persona):
    def __init__(self, nome, anno_nascita, corso_studio):
        super().__init__(nome, anno_nascita)
        self._corso_studio = corso_studio
    def __repr__(self):
        return f"Nome: {self._nome}, Anno di nascita: {self._anno_nascita}, Corso di studio: {self._corso_studio}"        
class Docente(Persona):
    def __init__(self, nome, anno_nascita, salario):
        super().__init__(nome, anno_nascita)
        self._salario = salario   
    def __repr__(self):
        return f"Nome: {self._nome}, Anno di nascita: {self._anno_nascita}, Salario: {self._salario}"
    

Studente1 = Studente("Mario", 2000, "Informatica")
Persona1 = Persona("Luigi", 1990)
Docente1 = Docente("Anna", 1985, 3000)
print(Studente1)
print(repr(Studente1))