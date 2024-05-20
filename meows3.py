"""
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")#sys kullanarak alacağımız girdilerde de (-n sayı) kullanarak kaç defa yazılacağını belirtebiliriz
else:
    print("usage: meows.py")
"""
# python meows3.py -n 3 yazdığımızda 3 kez meow yazdıracaktır


#terminale meows3.py -h ya da --help yazılırsa dosyanın nasıl kullanacağı hakkında fikir verir. 

import argparse #Bir şeyi parsellemek için kullanılan kütüphane 

parser = argparse.ArgumentParser(description = "Meow like a cat")
parser.add_argument("-n", default = 1, help = "Number of times to meow", type = int)# Default yazmamızın sebebi kullanıcıdan girdi almazsak yine de kaç kez yazdırmamız gerektiğini bilmemiz için
args = parser.parse_args()

for _ in range(args.n):
    print("meow")