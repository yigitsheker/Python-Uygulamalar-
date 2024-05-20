students = [
    {"name" = "Hermoine", "house" : "Gryffindor"},
    {"name" = "Harry", "house" : "Gryffindor"},
    {"name" = "Ron", "house" : "Gryffindor"},
    {"name" = "Draco", "house" : "Slytherin"},
]
"""
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
"""
# filter(function,elements in the sequence)

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)# Filter ile map'in farkı map her öğe için bir değer döndürür ama filter eğer bir öğeyi şartlı olarak bir listeye dahil etmek istersen kullanılır.

for gryffindor in sorted(gryffindors, key = lambda s: s["name"]): # Sözlükteki öğeleri sıralamak için
    print(gryffindor["name"])


# Dictionary Comprehensions

students2 = ["Hermoine","Harry","Ron"]

gryffindors2 = {student: "Gryffindor" for student in students2}

#[{"name" : student, "house": "Gryffindor"} for student in students2] yerine yukarıdakini kullandık

print(gryffindors2)

# enumerate(iterable, start = 0)

for i, student in enumerate(students2):
    print(i+1, student)