from lib.Account import Account
from lib.Transaction import Transaction
from datetime import datetime

account = Account()
account2 = Account()
today = datetime.today().strftime("%d/%m/%Y")

def test_deposit_with_zero_amount():
  assert account.add_transaction("deposit", 0) == "Amount must be positive"

def test_deposit_returns_a_transaction_object():
  deposit = account.add_transaction("deposit", 100)
  assert isinstance(deposit, Transaction)

# use doubles? test behaviour not state
def test_deposit_with_positive_amount():
  deposit = account.add_transaction("deposit", 100)
  assert deposit.amount == 100

def test_deposit_with_negative_amount():
  assert account.add_transaction("deposit", -100) == "Amount must be positive"

def test_deposit_with_string_input():
  assert  account.add_transaction("deposit", "100") == "Amount must be a number"

def test_deposit_with_array_as_input():
  assert account.add_transaction("deposit", []) == "Amount must be a number"

def test_deposit_with_none_as_input():
  assert account.add_transaction("deposit", None) == "Amount must be a number"

# use doubles? test behaviour not state
def test_multiple_deposits():
  deposit1 = account2.add_transaction("deposit", 100)
  deposit2 = account2.add_transaction("deposit", 200)
  assert account2.ledger == [[deposit1, 100], [deposit2, 300]]

def test_deposit_with_date_with_slashes():
  account = Account()
  deposit = account.add_transaction("deposit", 500, "10/10/2020")
  assert deposit.date == datetime.strptime("10/10/2020", '%d/%m/%Y')

def test_deposit_with_date_with_dashes():
  account = Account()
  deposit = account.add_transaction("deposit", 500, "10-10-2020")
  assert deposit.date == datetime.strptime("10-10-2020", '%d-%m-%Y')