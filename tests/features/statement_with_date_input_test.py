from lib.Account import Account
from lib.Statement import Statement

account = Account()
account.add_transaction("deposit", 500, '12/12/2020')
account.add_transaction("deposit", 500, '13/10/2020')
account.add_transaction("withdraw", 600, '15/10/2020')
statement = Statement.make(account)
print(statement)

account_2 = Account()
account_2.add_transaction("deposit", 500, '12-12-2020')
account_2.add_transaction("deposit", 500, '13-10-2020')
account_2.add_transaction("withdraw", 600, '15-10-2020')
statement = Statement.make(account)
print(statement)