from datetime import datetime
from lib.Validate import Validate
from lib.Transaction import Transaction

class Account:
  def __init__(self, start_bal = 0):
    self.balance = start_bal if Validate.is_number(start_bal) else 0
    self.ledger = []

  def add_transaction(self, transaction_type, amount, transaction_date=datetime.today()):
    if not transaction_date is self.add_transaction.__defaults__[0]:
      transaction_date = Validate.cast_to_datetime(transaction_date)
    if Validate.is_positive_number(amount):
      if transaction_type == "withdraw":
        if self.sufficient_funds(amount):
          amount = float(amount) * -1
        else:
          return "Insufficient Funds"
      amount = float(amount)
      self.balance += amount
      transaction = Transaction(amount, transaction_type, transaction_date)
      self.ledger.append([transaction, self.balance])
      return transaction
    return "Invalid Input"

  def sufficient_funds(self, amount):
    return self.balance - amount >= 0

