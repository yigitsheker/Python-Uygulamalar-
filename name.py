import sys
"""
try:
    print("Hello my name is", sys.argv[1])
except IndexError:                           Kullanıcıya bi argüman yazmadığını belirtiriz. Ama bu argümanların sayısını kullanıcıya belirtmek için şağıdaki yöntem kullanılır.
    print("Too few arguments")
""" 
"""                             
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) >2:
    print("Too many arguments")
else:                                       # Asıl komutu else koşolunun arkasına saklamak istemzsek aşağıdaki yöntem uygulanabilir.
    print("Hello my name is", sys.argv[1])
"""
"""
if len(sys.argv) <2:
    sys.exit("Too few arguments") # sys.exit programın belirtilen nokatsında çıknanızı sağlar. Böylece koşulların olmadığı yerde hata vermek yerine programdan daha erken atarak hata oluşturmaz. 
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello my name is", sys.argv[1])
"""
# Eğer daha fazla isim almak istersek
if len(sys.argv) <2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:# 1 değerinden başlamamızın sebebi sistem bu listede 0. indekse dosyanın adını verir. Dolayısıyla dosya adını yazdırmamak için bu yöntem kullanılır.
    print("Hello my name is", arg)
