with open("names.txt", "r") as file:
    """
    lines = file.readlines() # Kaydettiğimiz text dosyasını okutmak için kullanılır 

for line in lines:
    print("hello, ", line.rstrip())

    """ # Hem okuyup hem yazdırmanın daha kısa şekilde yapılması için aşağıdaki gibi yazılır.
    for line in file:
        print("hello, " , line.rstrip())