# -*- coding: utf-8 -*-

class BankAccount:
    def __init__(self,name,balance = 0.0):
        self.owner = name
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
hesap = BankAccount("Murat Aykurt",6000)

print(hesap.get_balance())
hesap.deposit(1500)
print(hesap.get_balance())
hesap.deposit(500)
print(hesap.get_balance())
hesap.withdraw(1250)
print(hesap.get_balance())