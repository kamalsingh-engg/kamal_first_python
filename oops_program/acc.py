class account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())



    def deposite(self,amount):
        self.balance =self.balance + amount

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


account = account("D://pycharm//gettingstarted//oops_program//balance.txt");
print(account.balance)
account.deposite(50)
print(account.balance)
account.commit()
