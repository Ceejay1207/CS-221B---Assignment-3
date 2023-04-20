from person import Person
class Teacher(Person):
    def __init__(self,department,position,college)-> None:
        self.department = department
        self.position = position
        self.college = college
        
    def getDept(self):
        return self.department
    
    def getPosition(self):
        return self.position
    
    def getCollege(self):
        return self.college
    
    
    
    
