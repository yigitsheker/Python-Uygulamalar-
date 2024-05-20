students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set() # Set methodu bir listeye benzer ancka içinde aynı elemanın kopyasını bulundurmaz. Bu yüzden sırayla seçtiğimiz öğrencilerin evlerini eklerken aynı evi ekler mi diye sorgulamadık çünkü kopyları otomatik olarak siler.
for student in students:
    houses.add(student["house"]) # set methodunda append'in muadili olarak add kullanılır.
    #if student["house"] not in houses: houses.append(student["house"]) Şeklinde de yazılabilirdi eğer set kullanmasaydık

for house in sorted(houses):
    print(house)