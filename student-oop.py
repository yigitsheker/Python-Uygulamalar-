class Student:
    def __init__(self, name, house, patronus): #house= None yapmamın sebebi eğer house objesini isteğe bağlı yapacağım anlamına gelir.
        if not name:
            raise ValueError("Missing name!")
        if house not in ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]:
            raise ValueError("Invalid house!")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self): #objelerin string  olarak algılanmasını sağlar ve otomatik olarak çağırılır.
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "Geyik"
            case "Otter":
                return "Su Samuru"
            case "Jack Russell Terrier":
                return "Teriyer"
            case "Snake":
                return "Yılan"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name!!!")
        self.name = name
    
    #Getter function
    @property
    def house(self):
        return self._house
    
    #Setter function
    @house.setter
    def house(self,house):
       # if house not in ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]:
            #raise ValueError("Invalid House!!!") Artık otomatik olarak kontrol ediyor
        self._house = house



def main():
    student = Student.get()
    #student.house = "Number Four, Privet Drive" # Eğer böyle kullanıcıdan gelen girdiye bir müdahale gelirse property kullanarak girdileri koruma altına alabiliriz.
    print("Expecto Patronum!")
    print(student.charm())

"""
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name,house,patronus)
"""
@classmethod
def get(cls):
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return cls(name,house,patronus)


if __name__ == "__main__":
    main()

# class int(x, base=10), class str(object=""), str.lower(), str.strip([chars]), list, list.append(), dict       gibi daha önce kullandığımız şeyler de aslında bir class'tı