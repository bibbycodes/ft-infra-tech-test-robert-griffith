from lib.Account import Account
from lib.Statement import Statement

account = Account()
account.deposit(500, '12/12/2020')
account.deposit(500, '13/10/2020')
account.withdraw(600, '15/10/2020')
statement = Statement.make(account)
print(statement)