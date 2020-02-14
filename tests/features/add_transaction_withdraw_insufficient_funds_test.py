from lib.Account import Account
from lib.Statement import Statement

account = Account()
print(account.add_transaction("withdraw", 500))