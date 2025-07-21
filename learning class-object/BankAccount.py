class BankAccount:
    def __init__(self,acc_no,pin,balance):
        self.__acc_no = acc_no
        self.__pin = pin
        self.__balance = balance
    

    def login(self):
        acc_no = int(input("enter acc no: "))
        pin = int(input("enter pin: "))
        enter = False
        if acc_no == self.__acc_no and pin == self.__pin:
            return(True)
        else:
            print("wrong login acc no  or pin")
            return(enter)
        
    def deposit(self,amount):
        if self.login() == True:
            self.__balance += amount
            print(f"deposit successfull, current balance: {self.__balance}")
        
    def withdraw(self,amount):
        if self.login() == True:
            if amount > self.__balance:
                print("not enough balance")
            else:
                self.__balance -= amount
                print("withdraw successful")

    def get_balance(self):
        if self.login() == True:
            print("current balance is ",self.__balance)



c1 = BankAccount(11234,1234,1000)

c1.deposit(5000)
print(c1.get_balance())
c1.withdraw(3000)

# # print(c1.__acc_no)
# # AttributeError: 'BankAccount' object has no attribute '__acc_no'

