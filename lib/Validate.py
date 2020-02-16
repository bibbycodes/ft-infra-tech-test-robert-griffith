from datetime import datetime

class Validate:
  def transaction(amount, transaction_type, balance):
    if not Validate.transaction_type(transaction_type):
      return False
    if not Validate.is_number(amount):
      return False
    if not Validate.is_positive(amount):
      return False
    if transaction_type == "withdraw":
      if not Validate.sufficient_funds(amount, balance):
        return False
    return True

  def error_message(amount, transaction_type, balance):
    if not Validate.transaction_type(transaction_type):
      return "Invalid Transaction Type"
    if not Validate.is_number(amount):
      return "Amount must be a number"
    if not Validate.is_positive(amount):
      return "Amount must be positive"
    if transaction_type == "withdraw":
      if not Validate.sufficient_funds(amount, balance):
        return "Insufficient Funds"
    return "Invalid Input"
  
  def date(date):
    if not Validate.date_format(date):
      return False
    return True
    
  def sufficient_funds(amount, balance):
    return balance - amount >= 0
  
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
  
  def date_format(date):
    if type(date) == float:
      return "timestamp"
    dashes = date.split("-")
    slashes = date.split('/')
    if Validate.array_includes_numbers(dashes) and len(dashes[-1]) == 4:
      return "dashes"
    if Validate.array_includes_numbers(slashes) and len(slashes[-1]) == 4:
      return "slashes"
    return False

  def transaction_type(transaction_type):
    if transaction_type in  ["withdraw", "deposit"]:
      return True
    return False
  
  def array_includes_numbers(array):
    if len(array) < 1 or not len(array) == 3:
      return False
    for item in array:
      is_number = Validate.cast_to_number(item)
      if not is_number:
        return False
    return True

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

  def date_is_supplied(account, transaction_date):
    if transaction_date == account.add_transaction.__defaults__[0]:
      return transaction_date
    return Validate.cast_to_datetime(transaction_date)
