from student import Student

class Grade(Student):
    def __init__(self, filipino, math, science, english) -> None:
        self.filipino = filipino
        self.math = math
        self.science = science
        self.english = english

    def getAverage(self):
        return (int(self.filipino) + int(self.math) + int(self.science) + int(self.english))/4