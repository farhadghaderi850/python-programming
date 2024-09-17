class bankaccount:
    def __init__(self , owner_name, account_number , balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Witharaw = " , amount)
        else:
            print("not enough balance")
    def deposit(self , amount):
        self.balance += amount
        print("deposit = " , amount)
        print("new balance = " , self.balance)
    def account_data(self):
        print("owner : " , self.owner_name)
        print("account number : " , self.account_number)
        print("account balance : " , self.balance)
account_example = bankaccount ("john" , "15324852" , 10000)
account_example.account_data()
account_example.deposit(700)
account_example.withdraw(300)
account_example.account_data()