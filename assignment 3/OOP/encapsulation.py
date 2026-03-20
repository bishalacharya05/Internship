#Encapsulation is the process of binding variables and methods inside the a class
#It helps to protect data from accidental modification

class account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
     
    def deposit(self,amount):
        self.balance +=amount
    
    def show(self):
        print(f"the total balance = {self.balance}")
        print(f"Account number ={self.acc_no}")
        
acc= account(123456,1000)
acc.deposit(500)
acc.show()
