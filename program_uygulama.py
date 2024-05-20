import random

ogrenciler = ["Yunus", "Emir", "Türkbey", "Yiğit", "Taha", "Onur", "Emir", "Metehan", "Berkan", "Mert"]
ogretmenler = ["Öğretmen A", "Öğretmen B", "Öğretmen C", "Öğretmen D", "Öğretmen E"]

atamalar = {}

for ogrenci in ogrenciler:
    ogretmen = random.choice(ogretmenler)
    if ogretmen in atamalar:
        if ogrenci not in ogretmen:
            atamalar[ogretmen].append(ogrenci)
    else:
        if ogrenci not in ogretmen:
            atamalar[ogretmen] = [ogrenci]
        else:
            continue 

a = 2


for ogretmen, ogrenci in atamalar.items():
    print(f"{ogretmen}'e atanan öğrenciler:")
    for ogrenci in ogrenciler:
        print(ogrenci)
    print()