from lib.Account import Account
from datetime import date

account = Account(300)
account2 = Account(1000)
account3 = Account()
today = date.today().strftime("%d/%m/%Y")

def test_withdraw_with_zero_amount():
  assert account.withdraw(0) == "Invalid Input"

def test_withdraw_with_positive_amount():
  assert account.withdraw(300) == [[-300, today]]

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
  assert account2.withdraw(200) == [[-300, today], [-200, today]]

def test_sufficient_balance_on_withdraw():
  assert account3.withdraw(300) == "Insufficient Funds"
