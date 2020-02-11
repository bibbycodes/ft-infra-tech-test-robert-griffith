from datetime import date
from lib.Validator import Validator
from lib.Transaction import Transaction

class Account:
  def __init__(self, starting_balance = 0):
    if Validator.validate_number(starting_balance):
      self.starting_balance = starting_balance
    else:
      self.starting_balance = 0
    self.balance = starting_balance
    self.ledger = []

  def deposit(self, amount):
    if Validator.validate_number(amount):
      return self.add_transaction("deposit", amount)
    else:
      return "Invalid Input"

  def withdraw(self, amount):
    if Validator.validate_number(amount):
      if self.sufficient_funds(amount):
        return self.add_transaction("withdraw", amount)
      else:
        return "Insufficient Funds"
    else:
      return "Invalid Input"

  def add_transaction(self, transaction_type, amount):
    today = date.today().strftime("%d/%m/%Y")
    if Validator.validate_number(amount):
      self.balance += amount
      transaction = Transaction(amount, transaction_type)
      self.ledger.append(transaction)
      return transaction
    else:
      return "Invalid Input"

  def sufficient_funds(self, amount):
    return self.balance - amount >= 0

    