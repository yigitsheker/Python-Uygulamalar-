import json
import requests
import sys

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term" + sys.argv[1])#linkin içindeki limit değeri şarkı limitini gösterir

#print(json.dumps(response.json(), indent = 2)) indent komutu yazılan şeylerin arasına 2 boşluk koyar. json() verilen linkin javascirpt söz dizimi şeklinde gözükmesini sağlar

a = response.json()
for result in a[results]:
    print(result["trackName"])# javascript görünümünde sözlük içinde sözlük olduğu için bu şekilde şarkıların isimlerini çağırabiliriz