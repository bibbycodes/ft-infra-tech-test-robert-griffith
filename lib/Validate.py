from datetime import datetime

class Validate:
  def check_input(amount, date):
    is_number = Validate.is_number(amount)
    is_positive = Validate.is_positive(amount)
    is_date = Validate.date_format(date)
    if False in [is_number, is_date, is_positive]:
      return False
    return True

  def is_positive_number(number):
    if not Validate.is_number(number):
      return False
    if not Validate.is_positive(number):
      return False
    return True

  def is_number(amount):
    return (type(amount) in [int, float])

  def is_positive(amount):
    amount = Validate.cast_to_number(amount)
    return amount > 0

  def cast_to_number(value):
    try:
      return float(value)
    except:
      return False
  
  # checks if format is dd/mm/yyyy or dd-mm-yyy
  # if already date object, return true
  # checks length of year is 4
  # checks if all values are numbers
  # change to validate using regex if you have time
  def date_format(date):
    if type(date) == float:
      return "timestamp"
    dashes = date.split("-")
    slashes = date.split('/')
    if Validate.check_array_includes_numbers(dashes) and len(dashes[-1]) == 4:
      return "dashes"
    if Validate.check_array_includes_numbers(slashes) and len(slashes[-1]) == 4:
      return "slashes"
    return False

  def transaction_type(transaction_type):
    if transaction_type in  ["withdraw", "deposit"]:
      return True
    return False
  
  def check_array_includes_numbers(array):
    if len(array) < 1 or not len(array) == 3:
      return False
    for item in array:
      is_number = Validate.cast_to_number(item)
      if not is_number:
        return False
    return True

  def transaction(amount, transaction_type):
    if Validate.transaction_type(transaction_type) == True and Validate.is_positive_number(amount):
      return True
    return False

  def cast_to_datetime(date_string):
    date_format = Validate.date_format(date_string)
    if date_format == "dashes":
      return datetime.strptime(date_string, '%d-%m-%Y')
    elif date_format == "slashes":
      return datetime.strptime(date_string, '%d/%m/%Y')
    elif date_format == 'timestamp':
      return datetime.fromtimestamp(date_string)
    else:
      return "Invalid date format"

    
