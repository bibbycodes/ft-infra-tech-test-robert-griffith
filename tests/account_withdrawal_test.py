from lib.Account import Account
from lib.Transaction import Transaction
from datetime import datetime

account = Account(300)
account_1 = Account(300)
account_2 = Account(1000)
account_3 = Account()
account_4 = Account(500)
today = datetime.today()

def test_withdraw_with_zero_amount():
  assert account.add_transaction("withdraw", 0) == "Invalid Input"

def test_withdrawal_is_a_transaction_object():
  withdrawal = account.add_transaction("withdraw", 200)
  assert isinstance(withdrawal, Transaction)

def test_withdraw_with_positive_amount():
  withdrawal = account_1.add_transaction("withdraw",300)
  assert withdrawal.amount == -300
  assert withdrawal.transaction_type == "withdraw"

def test_withdraw_with_negative_amount():
  assert account.add_transaction("withdraw", -300) == "Invalid Input"

def test_withdraw_with_string_input():
  assert account_4.add_transaction("withdraw","300") == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.add_transaction("withdraw", []) == "Invalid Input"

def test_withdraw_with_invalid_input():
  assert account.add_transaction("withdraw", None) == "Invalid Input"

def test_multiple_withdraws():
  withdrawal_1 = account_2.add_transaction("withdraw", 300)
  withdrawal_2 = account_2.add_transaction("withdraw", 200)
  assert account_2.ledger == [[withdrawal_1, 700], [withdrawal_2, 500]]

def test_sufficient_balance_on_withdraw():
  assert account_3.add_transaction("withdraw", 300) == "Insufficient Funds"
