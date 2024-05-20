name = input("What's your name?")

with open("names.txt", "a") as file:#Open komutu programa girilen girdilerin kaydedilmesi için kullanılır. names.txt adında dosya açıp onun içine girilen isimleri kaydeder.
                          # Eğer "a" yerine "w" simgesi koyarsak dosya yoksa bizim için oluşturur ve onu değiştirmemizi sağlar ancak programı üst üste çalıştırdığımızda kaydedilen isimleri yenileriyle değiştirir.
    file.write(f"{name}\n")

#file.close kullanarak dosyaları kapatabiliriz ancak unutabiliriz de bu işi otomatik olarak yapmak için with kullanılır.