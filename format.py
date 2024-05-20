import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # := işareti hem seğişken tanımlamamıza hem de o değişkenle alakalı bir soru sormamıza yarayan özellikte bir operatördür.
    last, first = matches.groups() # Burada matches içindeki parantez içlerini yani grupları belirttik ve onları last ve first adlı değişkenlere atadık.
    # last= matches.group(1) ve first = matches.group(2). Eğer bu değişkenleri bir daha kullanmayacaksak o değişkenleri yazmak yerine değişkenlerin değerlerini f stringimizin içine yazabiliriz.
    name = f"{first} {last}"