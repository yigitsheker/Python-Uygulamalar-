#Şimdi Sadece isimleri okutup yazdırmayacağız. Aynı zamanda alfabetik olarak sıralayacağız.

with open("names.txt") as file:# open varsayılan değeri "r" dir
    for line in sorted(file, reverse = True):# Eğer reverse değerini false yaparsak alfabetik olarak sıralar, true yaparsak alfabenin tesri şeklinde sıralar.
        print("hello, " , line.rstrip()) # Eğer text dosyasında daha fazla işlem yaptırmak istiyorsan (büyük harf olsun küçük harf olsun vs.) liste kullanarak yapmak daha iyi olablir.
    
"""                                        TIPKI BÖYLE
names= []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
    
"""   