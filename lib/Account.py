from datetime import datetime
from lib.Validate import Validate
from lib.Transaction import Transaction

class Account:
  def __init__(self, start_bal = 0):
    self.balance = start_bal if Validate.is_number(start_bal) else 0
    self.ledger = []

  def add_transaction(self, transaction_type, amount, transaction_date=datetime.today()):
    transaction_date = Validate.date_is_supplied(self, transaction_date)
    if Validate.amount(amount):
      amount = self.handle_amount(transaction_type, amount)
      self.balance += amount
      transaction = Transaction(amount, transaction_type, transaction_date)
      self.ledger.append([transaction, self.balance])
      return transaction
    return Validate.error_message(amount, transaction_date)

  def handle_amount(self,transaction_type, amount):
    if transaction_type == "withdraw":
      amount = amount * -1
    return float(amount)

