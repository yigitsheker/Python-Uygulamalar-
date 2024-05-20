"""
with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",") # Splitin ayırdığı sözcüklerden ilki yani 0 indexli olanları name değişkeninin içine 1 indexli olanlarsa city değişkeninin içine gidecek
        print(f"{name} is in {city}")
"""
# SIralı halde yazdırmak içinse alttaki gibi bir yöntem kullanılır.

students = []

with open("students.csv") as file:
    for line in file:
        name , city = line.strip().split(",")
        student = {"name" : name ,"city" : city}
        students.append(student)

# Sıralı yapmak için fonksiyon türetip key="get_name" olarak for döngüsünde sorted fonksiyonuna vereceğiz.
"""
def get_name(student):
    return student["name"]
"""        # Bu fonksiyon yerine lambda kullanılailir. eğer bu fonksiyon kullanılacaksa key = get_name yazılmalıdır


for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']}")