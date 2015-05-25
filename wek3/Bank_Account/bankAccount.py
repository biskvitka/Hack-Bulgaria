class BankAccount:
    def __init__ (self, name, start_balance, currency):
        if start_balance < 0:
            raise ValueError("You can't have negative amount of money in your bank account!")
        self.__name = str(name)
        self.__balance = __start_balance
        self.__currency = str(currency)
        self.__history = []

    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount < 0:
            raise ValueError ("You can't deposit negative amount!")
        self.balance += amount

    def balance(self):
        return self.__balance

    def withdraw(self,amount):
        if (amount <= __balance):
            self.__balance -= amount
            return True
        return False

    def __str__ (self):
        return "Bank account for {} with balance of {}{}".format(self.name,self.balance,self.currency)

    def __int__(self):
        return self.__balance

    def transfer_to(self,other, amount):
        if amount <= self_balance:
            self_balance -= amount
            other_balance -= amount
            return True
        return False

    def history(self):
        pass

