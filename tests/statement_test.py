from lib.Statement import Statement
from lib.Transaction import Transaction
from datetime import date
from lib.Account import Account

account_1 = Account()
account_2 = Account(1000)
account_3 = Account()
today_string = date.today().strftime("%d/%m/%Y")

def test_make_headers():
  assert Statement.headers() == 'date || credit || debit || balance\n'

def test_format_transaction_with_deposit():
  deposit = account_1.deposit(500)
  # should be mocking date
  expected_string = "{} || 500.00 || || 500.00\n".format(today_string)
  assert Statement.format_transaction([deposit, account_1.balance]) == expected_string

def test_format_transaction_with_withdrawal():
  withdrawal = account_2.withdraw(500)
  expected_string = "{} || || 500.00 || 500.00\n".format(today_string)
  assert Statement.format_transaction([withdrawal, account_1.balance]) == expected_string

def test_format_transaction_with_two_deposits():
  deposit_1 = account_3.deposit(500)
  deposit_2 = account_3.deposit(500)
  expected_string = "date || credit || debit || balance\n{} || 500.00 || || 500.00\n{} || 500.00 || || 1000.00".format(today_string, today_string)
  assert Statement.make(account_3) ==  expected_string
