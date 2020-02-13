from datetime import date
from lib.Validate import Validate
from lib.Transaction import Transaction

class Account:
  def __init__(self, start_bal = 0):
    self.balance = start_bal if Validate.is_number(start_bal) else 0
    self.ledger = []

  def deposit(self, amount):
    if Validate.is_positive(amount):
      return self.add_transaction("deposit", amount)
    return "Invalid Input"

  def withdraw(self, amount):
    if Validate.is_number(amount) and Validate.is_positive(amount):
      amount = float(amount)
      if self.sufficient_funds(amount):
        return self.add_transaction("withdraw", amount * -1)
      return "Insufficient Funds"
    return "Invalid Input"

  def add_transaction(self, transaction_type, amount):
    today = date.today().strftime("%d/%m/%Y")
    if Validate.is_number(amount):
      amount = float(amount)
      self.balance += amount
      transaction = Transaction(amount, transaction_type)
      self.ledger.append([transaction, self.balance])
      return transaction
    return "Invalid Input"

  def sufficient_funds(self, amount):
    return self.balance - amount >= 0

  def set_balance(balance):
    self.balance = balance
