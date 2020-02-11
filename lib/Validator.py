class Validator:
  def validate_number(amount):
    return (type(amount) in [int, float] and amount > 0)