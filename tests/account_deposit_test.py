from lib.Account import Account
from lib.Transaction import Transaction
from doubles import InstanceDouble, allow
from datetime import date

account = Account()
account2 = Account()
today = date.today().strftime("%d/%m/%Y")

def test_deposit_with_zero_amount():
  assert account.deposit(0) == "Invalid Input"

def test_deposit_returns_a_transaction_object():
  deposit = account.deposit(100)
  assert isinstance(deposit, Transaction)

# use doubles? test behaviour not state
def test_deposit_with_positive_amount():
  deposit = account.deposit(100)
  assert deposit.amount == 100

def test_deposit_with_negative_amount():
  assert account.deposit(-100) == "Invalid Input"

def test_deposit_with_string_input():
  assert account.deposit("100") == "Invalid Input"

def test_deposit_with_array_as_input():
  assert account.deposit([]) == "Invalid Input"

def test_deposit_with_none_as_input():
  assert account.deposit(None) == "Invalid Input"

# use doubles? test behaviour not state
def test_multiple_deposits():
  deposit1 = account2.deposit(100)
  deposit2 = account2.deposit(200)
  assert account2.ledger == [deposit1, deposit2]