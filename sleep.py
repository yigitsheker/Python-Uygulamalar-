def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Sheep" * i # return yerine yield(iterator = yineleyici) kullanmamızın sebebi eğer olurda bilgisayarın hafıza ve Ramini zorlayacak bir sayı girilirse tüm değerleri bir anda geri döndürmek yerine teker teker geri döndürür ve böylece program düzgünce çalışır.

if __name__ == "__main__":
    main()