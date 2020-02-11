class Account:
  def __init__(self, starting_balance = 0):
    if type((starting_balance)) in [int, float]:
      self.starting_balance = starting_balance
    else:
      self.starting_balance = 0
    self.balance = starting_balance

  def deposit(self, amount = 0):
    if type(amount) in [int, float] and amount >= 0:
      self.balance += amount
      return amount
    else:
      return "Invalid Input"