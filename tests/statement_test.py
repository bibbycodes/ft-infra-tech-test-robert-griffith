from lib.Statement import Statement
from lib.Transaction import Transaction
from datetime import date
from time import time
from lib.Account import Account
# should be mocking date

account_1 = Account()
account_2 = Account(1000)
account_3 = Account()
account_4 = Account(1000)
today_string = date.today().strftime("%d/%m/%Y")

def test_make_headers():
  assert Statement.headers() == 'date || credit || debit || balance\n'

def test_format_transaction_with_deposit():
  deposit = account_1.add_transaction("deposit", 500)
  expected_string = "{} || 500.00 || || 500.00\n".format(today_string)
  assert Statement.format_transaction([deposit, account_1.balance]) == expected_string

def test_format_transaction_with_withdrawal():
  withdrawal = account_2.add_transaction("withdraw", 500)
  expected_string = "{} || || 500.00 || 500.00\n".format(today_string)
  assert Statement.format_transaction([withdrawal, account_1.balance]) == expected_string

def test_format_transaction_with_two_deposits():
  deposit_1 = account_3.add_transaction("deposit", 500)
  deposit_2 = account_3.add_transaction("deposit", 500)
  expected_string = "date || credit || debit || balance\n{} || 500.00 || || 500.00\n{} || 500.00 || || 1000.00".format(today_string, today_string)
  assert Statement.make(account_3) ==  expected_string

def test_format_transaction_with_two_withdrawals():
  withdrawal_1 = account_4.add_transaction("withdraw", 500)
  withdrawal_2 = account_4.add_transaction("withdraw", 500)
  expected_string = "date || credit || debit || balance\n{} || || 500.00 || 500.00\n{} || || 500.00 || 0.00".format(today_string, today_string)
  assert Statement.make(account_4) ==  expected_string

def test_make_statement_with_deposits_adn_withdrawals():
  account = Account()
  account.add_transaction("deposit", 500)
  account.add_transaction("deposit", 500)
  account.add_transaction("withdraw", 600)
  statement = Statement.make(account)
  expected_string = "date || credit || debit || balance\n{} || 500.00 || || 500.00\n{} || 500.00 || || 1000.00\n{} || || 600.00 || 400.00\n".format(today_string, today_string, today_string)


def test_format_transaction_with_timestamp():
  epoch = (time())
  transaction = account_1.add_transaction("deposit", 500, epoch)
  assert Statement.format_transaction([transaction, account_1.balance]) == "{} || 500.00 || || 1000.00\n".format(today_string)
