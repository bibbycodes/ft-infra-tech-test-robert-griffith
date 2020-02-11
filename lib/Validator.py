def validate(amount):
  return (type(amount) in [int, float] and amount > 0)