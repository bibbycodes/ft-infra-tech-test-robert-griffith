from datetime import datetime

class Validate:
  def is_number(amount):
    amount = Validate.cast_to_number(amount)
    return (type(amount) in [int, float])

  def is_positive(amount):
    amount = Validate.cast_to_number(amount)
    return amount > 0

  def cast_to_number(value):
    try:
      return float(value)
    except:
      return False

  def check_date_format(date_string):
    dashes = date_string.split("-")
    slashes = date_string.split('/')
    if Validate.check_array_includes_numbers(dashes):
      return "dashes"
    if Validate.check_array_includes_numbers(slashes):
      return "slashes"
    return False

  def check_array_includes_numbers(array):
    if len(array) < 1:
      return False
    for item in array:
      is_number = Validate.cast_to_number(item)
      if not is_number:
        return False
    return True

  def cast_to_datetime(date_string):
    date_format = check_date_format(date_string)
    if date_format == "dashes":
      return datetime.strptime(date_string, '%d-%m-%Y')
    elif date_format == "slashes":
      return datetime.strptime(date_string, '%d/%m/%Y')
    else:
      return "Invalid date format"

    
