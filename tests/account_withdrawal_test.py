from lib.Account import Account
from lib.Transaction import Transaction
from datetime import date

account = Account(300)
account2 = Account(1000)
account3 = Account()
today = date.today()

def test_withdraw_with_zero_amount():
  assert account.withdraw(0) == "Invalid Input"

def test_withdrawal_is_a_transaction_object():
  withdrawal = account.withdraw(200)
  assert isinstance(withdrawal, Transaction)

def test_withdraw_with_positive_amount():
  withdrawal = account.withdraw(300)
  assert withdrawal.amount == 300
  assert withdrawal.date == date.today
  assert withdrawal.transaction_type == "withdraw"

def test_withdraw_with_negative_amount():
  assert account.withdraw(-300) == "Invalid Input"

def test_withdraw_with_string_input():
  assert account.withdraw("300") == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.withdraw([]) == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.withdraw(None) == "Invalid Input"

def test_multiple_withdraws():
  withdrawal1 = account2.withdraw(300)
  withdrawal2 = account2.withdraw(200)
  assert account2.ledger == [withdrawal1, withdrawal2]

def test_sufficient_balance_on_withdraw():
  assert account3.withdraw(300) == "Insufficient Funds"
