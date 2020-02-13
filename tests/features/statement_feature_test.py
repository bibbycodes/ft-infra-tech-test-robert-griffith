from lib.Account import Account
from lib.Statement import Statement

account = Account()
account.deposit(500)
account.deposit(500)
account.withdraw(600)
statement = Statement.make(account)
print(statement)

