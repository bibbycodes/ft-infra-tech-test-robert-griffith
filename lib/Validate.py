class Validate:
  def is_number(amount):
    return (type(amount) in [int, float])

  def is_positive(amount):
    return amount > 0