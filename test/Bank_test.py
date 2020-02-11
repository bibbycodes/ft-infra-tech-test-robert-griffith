from lib.Account import Account

def test_init_account_instance():
  account = Account()
  assert account.starting_balance == 0