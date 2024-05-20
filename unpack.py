"""
def total(galleons, sickles,knuts):
    return (galleons *17 + sickles)*29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")# *coins coins listesinin içini açar ve senin teker teker değer vermene gerek kalmadan onları fonksiyondaki değerlere atar. Sözlüklerde kullanmak için **coins şeklinde kullanılmalıdır.

"""

def f(*argv, **kwargs): # *argv = Değişken sayıda argüman aldığını belirtmek için kullanılır. **kwargs = İsteğe bağlı olarak çağırılabilen adlandırılmış parametreler ve kendi bireysel adlarıyla çağrılmak için kullanılır.
    # *args positional argümanlar için **kwargs named argümanları için kullanılır. Yani *argvs argümanları -> 100, 50, 25  **kwargs argümanları -> galleons = 100, sickles = 50, knuts = 25 ve bunları sözlük şeklinde saklar
    print("Named: " , kwargs)

f(galleons = 100, sickles = 50, knuts = 25)