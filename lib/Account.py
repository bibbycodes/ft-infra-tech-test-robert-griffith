from datetime import datetime
from lib.Validate import Validate
from lib.Transaction import Transaction

class Account:
  def __init__(self, start_bal = 0):
    self.balance = start_bal if Validate.is_number(start_bal) else 0
    self.ledger = []

  def add_transaction(self, transaction_type, amount, transaction_date=datetime.today()):
    transaction_date = Validate.date_supplied(self, transaction_date)
    if Validate.is_positive_number(amount):
      amount = self.handle_amount(transaction_type, amount)
      self.balance += amount
      transaction = Transaction(amount, transaction_type, transaction_date)
      self.ledger.append([transaction, self.balance])
      return transaction
    return "Invalid Input"

  def handle_amount(self,transaction_type, amount):
    if transaction_type == "withdraw":
      if Validate.sufficient_funds(self, amount):
        amount = float(amount) * -1
      else:
        print("Insufficient Funds")
    return float(amount)

