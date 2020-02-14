from lib.Account import Account
from lib.Statement import Statement

account = Account(4000)
account.add_transaction("withdraw", 500)
account.add_transaction("withdraw", 500)
statement = Statement.make(account)
print(statement)