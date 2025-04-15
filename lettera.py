class Letter:
            def __init__(self, letterFrom, letterTo):
                self._letterFrom = letterFrom
                self._letterTo = letterTo
                self._lines = []

            def addLine(self, line):
                self._lines.append(line)

            def getText(self):
                letter_text = f"Dear {self._letterTo},\n\n"
                letter_text += "\n".join(self._lines)
                letter_text += f"\n\nSincerely,\n\n{self._letterFrom}"
                return letter_text
                
my_letter = Letter("Mary", "John")
my_letter.addLine("I am sorry we must part.")
my_letter.addLine("I wish you all the best.")
                   
print(my_letter.getText())