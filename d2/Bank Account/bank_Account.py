# class BankAccount:
#     # don't forget to add some default values for these parameters!
#     def __init__(self, int_rate, balance): 
#         self.balance = 0
#         self.int_rate = 1.10
#         # your code here! (remember, instance attributes go here)
#         # don't worry about user info here; we'll involve the User class soon
#     def deposit(self, amount):
#         amount = int(input('Enter amount:'))
#         self.balance += amount
#         print(amount)
#     def withdraw(self, amount):
#         if(amount>self.balance):
#             print('Insufficient funds: Charging a $5 fee')
#             self.balance -= 5
#         else:
#             self.balance -= amount
#             print(amount)
#     def display_account_info(self):
#         print(self.amount)
#     def yield_interest(self):
#         if(self.balance > 0):
#             self.balance *= self.int_rate
#             print(self.balance)






class Bank_Account:
    def __init__(self):
        self.balance = 0
        self.int_rate = 1.10
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited: ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(amount)
    def display_account_info(self):
        print("Net Available Balance=",self.balance)
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= self.int_rate
            print(amount)

b= Bank_Account()


b.deposit()
b.withdraw()
b.display_account_info()
b.yield_interest()
