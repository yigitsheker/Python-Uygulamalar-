import random 

class Hat:
    #def __init__(self):        Böyle de kullanılabilir.
        #self.houses = ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]
    houses = ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"] #Sınıfların da listeleri vardır

    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")