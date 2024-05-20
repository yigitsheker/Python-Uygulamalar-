class Cat:
    MEOWS = 3 # Eğer bir değişkene dokunulmaması gerektiğini belirtmek istiyorsak hepsini büyük harfle yazarak onun kesin yani constant bir değişken olduğunu belirtmeliyiz.

    def meows(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()