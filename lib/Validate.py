class Validate:
  def number(amount):
    return (type(amount) in [int, float] and amount > 0)