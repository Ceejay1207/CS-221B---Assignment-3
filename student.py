from person import Person
class Student(Person):
    def __init__(self,id,last_name,first_name,middle_name,type,year,course,section):
        super().__init__(id,last_name,first_name,middle_name,type)
        self.year = year
        self.course = course
        self.section = section
        
    def getStud(self):
        return self.year +'-'+ self.course +'-'+ self.section