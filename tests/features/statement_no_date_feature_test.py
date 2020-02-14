from lib.Account import Account
from lib.Statement import Statement

account = Account()
account.add_transaction("deposit", 1000)
account.add_transaction("withdraw", 500)
account.add_transaction("withdraw", 400)
account.add_transaction("deposit", 1000)
statement = Statement.make(account)
print(statement)

