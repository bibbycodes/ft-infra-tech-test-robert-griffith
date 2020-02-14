# from datetime import date
from lib.Validate import Validate

class Transaction:
  def __init__(self, amount, transaction_type, date):
    self.date = date
    self.transaction_type = transaction_type
    self.amount = amount