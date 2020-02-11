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
    if self.validate(amount) and amount > 0:
      return self.add_transaction("deposit", amount)
    else:
      return "Invalid Input"

  def withdraw(self, amount):
    if self.validate(amount) and amount > 0:
      return self.add_transaction("withdraw", amount)
    else:
      return "Invalid Input"

  def validate(self, amount):
    return (type(amount) in [int, float])

  def add_transaction(self, transaction_type, amount):
    today = date.today().strftime("%d/%m/%Y")
    if transaction_type == "withdraw":
      amount = amount * -1
    if self.validate(amount):
      self.balance -= amount
      self.ledger.append([amount, today])
      return self.ledger
    else:
      return "Invalid Input"
    