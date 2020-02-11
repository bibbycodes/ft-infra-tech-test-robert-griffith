from datetime import date

class Account:
  def __init__(self, starting_balance = 0):
    if self.validate(starting_balance):
      self.starting_balance = starting_balance
    else:
      self.starting_balance = 0
    self.balance = starting_balance
    self.ledger = []

  def deposit(self, amount):
    if self.validate(amount):
      return self.add_transaction("deposit", amount)
    else:
      return "Invalid Input"

  def withdraw(self, amount):
    if self.validate(amount):
      if self.sufficient_funds(amount):
        return self.add_transaction("withdraw", amount)
      else:
        return "Insufficient Funds"
    else:
      return "Invalid Input"

  def validate(self, amount):
    return (type(amount) in [int, float] and amount > 0)

  def add_transaction(self, transaction_type, amount):
    today = date.today().strftime("%d/%m/%Y")
    if self.validate(amount):
      if transaction_type == "withdraw":
        amount = amount * -1
      self.balance += amount
      self.ledger.append([amount, today])
      return self.ledger
    else:
      return "Invalid Input"

  def sufficient_funds(self, amount):
    return self.balance - amount >= 0

    