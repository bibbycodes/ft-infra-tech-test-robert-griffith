from lib.Account import Account

def test_init_account_instance():
  account = Account()
  assert account.starting_balance == 0

def test_init_account_instance_with_starting_balance():
  account = Account(300)
  assert account.starting_balance == 300