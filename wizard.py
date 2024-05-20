class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name





class Student(Wizard):# Student classının Wizard classındaki bütün özelliklere sahip olmasını sağlar.
    def __init__(self, name, house):
        super()__init__(name) # super() Bir önceki classın super class olduğunu belirtir ve o super classın içine erişmemizi sağlar.
        self.house = house



class Professor(Wizard):
    def __init__(self, name, subject):
        super()__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defence Against the Dark Arts")