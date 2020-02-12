class Validate:
  def is_number(amount):
    amount = Validate.cast_to_number(amount)
    return (type(amount) in [int, float])

  def is_positive(amount):
    amount = Validate.cast_to_number(amount)
    return amount > 0

  # this could cause issues
  def cast_to_number(value):
    try:
      return float(value)
    except:
      return False
    
