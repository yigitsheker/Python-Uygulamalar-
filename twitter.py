import re

url = input("URL of your Twitter page: ")

#re.sub(pattern, replace, string, count=0, flags =0 )

username = re.sub(r"^(https?://)?(www\.)?twitter\.com","",url)

#print(f"Username: {username}")

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/([a-z0-9_]+)$", url, re.IGNORECASE):
    if matches.group(1) == "com": #Eğer .com değil de başka bir ifade kullanılırsa diye
        print(f"Username:", matches.group(1))

# re.search ifadesinin daha etkili olma sebebi olur da bi manyak twitter linki vermek yerine başka bir site linki verirse ekrana bir şey yazdırmamak

#?: kullanılmasını sebebi eğer parantez içine alınacak bir ifade var ama geri döndürülmesine gerek yoksa (?:) kullanırız.Bunu yaptıktan sonra orası bir grup olarak sayılmaz yani yazdırırken group(1) deriz ancak o 2. gruba gider.

#re.split(pattern, string, maxsplit = 0, flags = 0) Birden fazla karakter kulllanarak string bir ifadeyi ayırmamıza yarar.

#re.findall(pattern, string, flags = 0) Aynı simgenin birden çok kopyasını bir stringte farklı yerlerdde aramamıza yarar.