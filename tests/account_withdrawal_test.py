from lib.Account import Account
from datetime import date

account = Account()
account2 = Account()
today = date.today().strftime("%d/%m/%Y")

def test_withdraw_with_zero_amount():
  assert account.withdraw(0) == "Invalid Input"

def test_withdraw_with_positive_amount():
  assert account.withdraw(300) == [[300, today]]

def test_withdraw_with_negative_amount():
  assert account.withdraw(-300) == "Invalid Input"

def test_withdraw_with_string_input():
  assert account.withdraw("300") == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.withdraw([]) == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.withdraw(None) == "Invalid Input"

def test_multiple_withdraws():
  account2.withdraw(300)
  assert account2.withdraw(200) == [[300, today], [200, today]]
