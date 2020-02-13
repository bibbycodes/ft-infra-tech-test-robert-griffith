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
    if Validate.cast_to_number(date_string.split("-")[0]):
      return "dashes"
    if Validate.cast_to_number(date_string.split("/")[0]):
      return "slashes"
    return False

  def cast_to_datetime(date_string):
    date_format = check_date_format(date_string)
    if date_format == "dashes":
      return datetime.strptime(date_string, '%d-%m-%Y')
    elif date_format == "slashes":
      return datetime.strptime(date_string, '%d/%m/%Y')
    else:
      return "Invalid date format"

    
