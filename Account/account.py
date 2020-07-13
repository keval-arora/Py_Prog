#account.py

from decimal import Decimal

class Account:
    """This is the main Account Class"""
    
#Account class Constructor:
    def __init__(self, name = ' ', balance = Decimal(0.00)):
        
        if balance < Decimal('0.00'):
            raise ValueError('Initialize balance with amount greater than ZERO')
        else:
            self.name = name
            self.balance = balance

#Getters & Setters
    @property
    def name(self):
        print("Inside name getter")
        
        return self._name
    
    @name.setter
    def name(self, name):
        print("Inside name setter")
        self._name = name
        
    
    @property
    def balance(self):
        print("Inside bal getter")
        
        return self._balance
    

    @balance.setter
    def balance(self, balance):
        print("Inside bal setter")
        
        if balance < Decimal('0.00'):
            raise ValueError('Initialize balance with amount greater than ZERO') 
        else:
            self._balance = balance
    
    
#Instance method:
    def deposite(self, amount):
        """Deposit the amount in account object"""    
        if amount < Decimal('0.00'):
            raise ValueError('Please enter amount greater than ZERO')
        else:
            self.balance += amount

    def withdraw(self, amount):
        """Withdraw the amount in account object"""      
        if amount < Decimal('0.00'):
            raise ValueError('Please enter amount greater than ZERO')
        else:
            self.balance -= amount 
            
#String Formatted Output:
    def __str__(self):
        """Withdraw the amount in account object"""
        return (f"Account name: {self.name}, Current Balance: {self.balance}")