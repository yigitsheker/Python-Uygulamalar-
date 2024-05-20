import csv
                         # Olurda bir durumda bir satırda birden fazla virgül kullanırsak reader kullanarak bu işi çözebiliriz çünkü reader virgülün tırnak içinde mi olup olmadığına dikkat eder.
students= []

with open("students.csv") as file:
    reader = csv.DictReader(file) #  reader csv dosyalarındaki metinlerin okunması için yapılmış bir komut. DictReader kullanılmasının sebebi değişiklikler karşı daha dayanıklı bir dosya oluşturmak. Birisi csv dosyasını değiştirse dahi name ve home değerlerini tam tersine çevirmek gibi DictReader sayesinde çıktı değişmez.
    for row in reader:
        students.append(row)


for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")