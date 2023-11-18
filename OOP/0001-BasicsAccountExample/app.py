# Understand OOP in Python, __init__, and super() | Python for Bankers 3
# https://www.youtube.com/watch?v=pvxj9bq7aW0
# More Python OOP concepts, methods, & calculating interest rates! | Python for Bankers 4
# https://www.youtube.com/watch?v=zHJJy14vAfY


from datetime import datetime


class Account:
    total_accounts = 0
    interest_rate = 0.04        # this is an ATTRIBUTE
    
    def __init__(self, act_no, act_balance, type):
        self.act_no = act_no
        self.act_balance = act_balance
        self.type = type
        self.created_date = datetime.now()
        Account.total_accounts += 1
        
    def returns(self, year):          # this is a METHOD
        # self.year = year
        # self.act_balance_over_time = self.act_balance * (1+self.interest_rate)**self.year
        # return f"Your balance is worth {self.act_balance_over_time} in {self.year} year(s)."
        if self.type == "multiplier":
            return f"Account {self.act_no}: Congratulations! You earn an extra 1% and your balance will be {round(self.act_balance * (1 + self.interest_rate + 0.01) ** year, 2)} in {year} years(s)."     # in a single line    
        return f"Account {self.act_no}: Your balance is worth {round(self.act_balance * (1 + self.interest_rate) ** year, 2)} in {year} years(s)."     # in a single line
        
        
class MultiCurrencyAccount(Account):        # inheritance >>> e.g. total_accounts is also inherited from the parent
    interest_rate = 0.01
    def __init__(self, act_no, act_balance, type, currencies):
        super().__init__(act_no, act_balance, type)
        self.currencies = currencies


print(Account.total_accounts)
myaccount = Account(55550005, 100, "savings")
mca = MultiCurrencyAccount(55550006, 500, "investment", ["SGD", "IDR", "USD"])
print(mca.created_date)
print(mca.currencies)

print(Account.total_accounts)
print(mca.interest_rate)

print(myaccount.interest_rate)
print(myaccount.returns(2))

newaccount = Account(55558888, 500, "multiplier")
print(newaccount.returns(2))