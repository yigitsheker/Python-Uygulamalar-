# Email Doğrulama

#Düzenli ifadeleri içe aktarıp kullanabileceğimiz bazı özellikler var

#re.search(pattern, string, flags = 0)

#Özel sembollerle pattern yani kalıpları tanımlayabiliriz. Örneğin;
"""
. = Herhangi bir karakteri temsil etmek için kullanılır
* = Var olan bir karakterin 0 veya daha fzzla kez tekrar edip etmemesi
+ = Var olan bir karakterin 0 veya daha fzzla kez tekrar edip etmemesi. Yani en az bir tane olması sonrasında fazla olsa da olur
? = bir karakterden 1 tane olması ya da hiç olmamasını ister
{m} = Belirtilen karakterden m tekrar istediğimizi belirtir
{m,n} = Belirtilen karakterden m'den n'ye kadar tekrar etmesini ister              Eğer olur da aratmak istediğimiz ifade yukarıdaki sembollerden birini taşırsa onun özelliğini kullanmak yerine o işareti sorgulamak için \ kullanılır. (r".+@+\.edu") gibi başa da r gelmesi lazım
^ = str ifadesinin başındaki karakterileri eşleştirir (Yazının başı)
$ = str ifadesinin sonundaki karakterleri veya yeni satır başındaki karakterleri eşleştirmek için kullanılır. (Yazının sonu)
[] = Özel olarak aramak istediğiniz bir veya daha fazla karakter için 
[^] = İçine yazılan karakter hariç olmalı aradığımız yazıda 
[a-zA-Z0-9_] = a'dan z'ye her harfin ve 0'dan 9'a heer rakamın ve alttan tirenin bulunabileceğini belirtir.(Büyük küçük fark etmez)
\w = Yukarıdakiyle aynı anlamı taşır, kıısaltmasıdır.
\d = Herhangi bir ondalık sayı için kullanılır.
\D = \d'nin tersi olarak ondalık sayı olmaması için kullanılır
\s = Boşluk karakterleri için kullanılır.
\S = Boşluk karakterleri olmaması için kullanılır
\W = \w'daki karakterler olmasın diye kullanılır
Eğer sadece .edu değil de .com gibi de aratmak istiyorsak (edu|com) yapılmalıdır

Flags

re.IGNORECASE = Büyük küçük harf görmezden gelinir.
re.MULTILINE = Birden fazla satırla girdi alabilmek için kullanılır
re.DOTALL = Yukarıyla aynı
"""

import re

email = input("What's your email?")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")