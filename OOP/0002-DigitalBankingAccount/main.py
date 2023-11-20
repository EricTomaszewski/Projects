# How to create a banking system using Object Oriented Programming in python for beginners
# https://www.youtube.com/watch?v=xTh-ln2XhgU

# Parent Class: User
# Child  Class: Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits, withdraw, view_balance


# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):         # has access to all info from __init__
        print("Personal details")
        print("")
        print("Name   ", self.name)
        print("Age    ", self.age)
        print("Gender ", self.gender)
        print("")
        
        
# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated: ", self.balance)
        print("")
        
    def withdrawal(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds : Balance available: £", self.balance)
            print("")
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated:       £", self.balance)
            print("")
    
    def view_balance(self):
        self.show_details()         # inherited from User class
        print("Account balance:       £", self.balance)
        print("")
        print("")
        
        

Eric = User("Eric", 100, "Male")
Eric.show_details()
# but deposit(), withdrawal(), etc. does not work on this unless initialised as Bank()

Eric = Bank("Eric", 39, "Male")
Eric.show_details()
Eric.deposit(100)
Eric.deposit(400)
Eric.withdrawal(200)
Eric.withdrawal(500)
Eric.view_balance()

Gosia = Bank("Gosia", 40, "Female")
Gosia.show_details()