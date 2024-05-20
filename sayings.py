def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#main() şeklinde fonksiyonu ana fonksiyonu en sonda çağırırsak herhangi başka bir dosyada bu dosyayı içe aktarırken istemesekte ana fonksiyon çalışır. Çalışmaması için aşağıdaki şekilde yazılmalıdır.

if __name__=="__main__":
    main()