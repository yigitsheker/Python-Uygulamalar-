def meow(n: int) -> str:# n olarak belirtilen şeyin bir int değer olması gerektiğini söyler
    return "meow\n" *n # -> str demek bir str değerin geri döndürüleceğini belirtir
    #for _ in range(n):
    #   print("meow")

# mypy kullanarak programı çalıştırmadan önce "mypy meow2.py" yazarak hata var mı yok mu kontrol edebilirsin. Mypy için ipuçları koyarsın tıpkı ->str veya :int gibi o sana hatanın ne olduğunu temiz bir şekilde anlatır

number: int = int(input("Number: ")) #number değişkeinin de int değeri olması gerektiğini belirtir.
meows: str = meow(number)
print(meows, end = "") #sys kullanarak alacağımız girdilerde de (-n sayı) kullanarak kaç defa yazılacağını belirtebiliriz