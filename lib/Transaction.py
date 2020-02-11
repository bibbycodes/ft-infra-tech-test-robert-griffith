from datetime import date
from lib.Validator import validate

class Transaction:
  def __init__(self, amount, transaction_type, date = date.today):
    self.date = date
    self.transaction_type = transaction_type
    if validate(amount):
      self.amount = amount
    else:
      self.amount = 0