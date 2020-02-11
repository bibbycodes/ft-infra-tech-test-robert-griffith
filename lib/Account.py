from datetime import date

class Account:
  def __init__(self, starting_balance = 0):
    if type((starting_balance)) in [int, float]:
      self.starting_balance = starting_balance
    else:
      self.starting_balance = 0

    self.balance = starting_balance
    self.ledger = []

  def deposit(self, amount):
    today = date.today().strftime("%d/%m/%Y")
    if type(amount) in [int, float] and amount > 0:
      self.balance += amount
      self.ledger.append([amount, today])
      return self.ledger
    else:
      return "Invalid Input"

  def withdraw(self, amount):
    today = date.today().strftime("%d/%m/%Y")
    if type(amount) in [int, float] and amount > 0:
      self.balance -= amount
      self.ledger.append([amount, today])
      return self.ledger
    else:
      return "Invalid Input"