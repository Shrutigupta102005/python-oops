class BankAccount:
    def __init__(self,account_number,owner,balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance 
    
    def display_balance(self):
        print(f"account_number:{self.account_number} \nowner:{self.owner}\n  balance:{self.balance}")

    def deposit(self,amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            return (f"withdrawing of ${amount} succesfully. New Balance: ${self.balance}.")
        else:
            return("insufficient balance")
        
    def monthly_statement(self):
        return "Monthly statement: No interest or fees applied."

class checkingaccount(BankAccount):
    def __init__(self, account_number,owner,balance=0,overdraft_limit=500):                                        #jbb yeh inheritance huga hi tuh hmm dubara kyu attributes define kar rahe hai 
        super().__init__(account_number,owner,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Exceeded overdraft limit"
        

if __name__ == "__main__":
    name = input("enter the number")
    account_number = 100238202822        # acc_num kyu liya??
    ac = BankAccount(account_number, name)
    while 1:
        print(''' menu
              1. Deposit
2. Withdraw
3. Check balance
4. account info
5. Exit
              ''')
choice = int(input('Enter the choice 1/2/3/4/5 '))
if choice == 5:
    print("ok")
elif choice==4:
    print(ac.getAccInfo())
elif choice==3:
    print(ac.checkBalance())
elif choice==2:
    amt=int(input("Enter amount: "))
    print(ac.withdraw(amt))
elif choice==1:
    amt=int(input("Enter amount: "))
    print(ac.deposit(amt))
else:
    print("Invalid input. Choose from the options below: ")
            