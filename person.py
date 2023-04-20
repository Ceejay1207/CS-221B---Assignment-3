class Person:
    def __init__(self,id,last_name,first_name,middle_name,type):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.type = type
    
    def getName(self):
        return (f'{self.last_name},{self.first_name},{self.middle_name}')