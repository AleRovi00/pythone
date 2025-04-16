class student:
    def __init__(self, name, surname,):
        self._name = name
        self._surname = surname
        self._score = 0
        self._quiz = 0

    def getName(self):
        return self._name + " " + self._surname
    def addQuiz(self, score):
        self._score += score
        self._quiz += 1
    def getTotalScore(self):
        return self._score
    def getAverageScore(self):
        if self._quiz == 0:
            #return 0
            raise ValueError(f"lo studente {self._name} {self._surname} non ha fatto nessun quiz")
        return self._score / self._quiz

ale= student("Alessandro", "Rossi")
ale.addQuiz(10)
ale.addQuiz(8)
ale.addQuiz(9)
print(ale.getName())
print(ale.getTotalScore())
print(ale.getAverageScore())

marco= student("Marco", "Bianchi")
print(marco.getAverageScore())