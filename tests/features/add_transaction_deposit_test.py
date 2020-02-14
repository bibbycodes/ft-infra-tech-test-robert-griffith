from lib.Account import Account
from lib.Statement import Statement

account = Account()
account.add_transaction("deposit", 500)
account.add_transaction("deposit", 500)
statement = Statement.make(account)
print(statement)