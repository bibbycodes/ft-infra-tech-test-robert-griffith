from datetime import date
from lib.Validate import Validate
from lib.Transaction import Transaction

class Account:
  def __init__(self, start_bal = 0):
    self.balance = start_bal if Validate.number(start_bal) else 0
    self.ledger = []

  def deposit(self, amount):
    return self.add_transaction("deposit", amount)

  def withdraw(self, amount):
    if self.sufficient_funds(amount):
      return self.add_transaction("withdraw", amount)
    return "Insufficient Funds"

  def add_transaction(self, transaction_type, amount):
    today = date.today().strftime("%d/%m/%Y")
    if Validate.number(amount):
      self.balance += amount
      transaction = Transaction(amount, transaction_type)
      self.ledger.append(transaction)
      return transaction
    return "Invalid Input"

  def sufficient_funds(self, amount):
    return self.balance - amount >= 0