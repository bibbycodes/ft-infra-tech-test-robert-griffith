from lib.Account import Account
account = Account()
account2 = Account()

def test_deposit_with_zero_amount():
  assert account.deposit(0) == "Invalid Input"

def test_deposit_with_positive_amount():
  assert account.deposit(100) == [100]

def test_deposit_with_negative_amount():
  assert account.deposit(-100) == "Invalid Input"

def test_deposit_with_string_input():
  assert account.deposit("100") == "Invalid Input"

def test_deposit_with_invalid_input():
  assert account.deposit([]) == "Invalid Input"

def test_deposit_with_invalid_input():
  assert account.deposit(None) == "Invalid Input"

def test_multiple_deposits():
  account2.deposit(100)
  assert account2.deposit(200) == [100, 200]