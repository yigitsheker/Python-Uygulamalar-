"""
balance = 0

# Fonksiyonların dışına yazılan değişkenler global değişkenlerdir ve değiştirilebilmesi için global komutu kullanılmalıdır.

def main():
    print("Balance: ",balance)
    deposit(100)# Parayı yatırmak
    withdraw(50)# Parayı çekmek
    print("Balance: ",balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ =="__main__":
    main()
"""

class Account:
    def __init__(self):
        self._balance = 0 # _ işareti bu değişkenin önemli oldğunu ve bu değişkenle uğraşılmaması gerektiğini gösterir

    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account._balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account._balance)

if __name__ == "__main__":
    main()