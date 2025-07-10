class BankAccount:
    def __init__(self,acc_no,balance):
        self.__acc_no = acc_no
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"deposit successfull, current balance: {self.__balance}")
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("not enough balance")
        else:
            self.__balance -= amount
            print("withdraw successful")

    def get_balance(self):
        print("current balance is ",self.__balance)

c1 = BankAccount(11234,1000)

c1.deposit(10000)
print(c1.get_balance())
c1.withdraw(3000)

# print(c1.__acc_no)
# AttributeError: 'BankAccount' object has no attribute '__acc_no'

print(c1.get_balance())
