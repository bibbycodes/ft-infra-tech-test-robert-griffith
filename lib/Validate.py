from datetime import datetime

class Validate:
  def check_input(amount, date):
    is_number = Validate.is_number(amount)
    is_positive = Validate.is_positive(amount)
    is_date = Validate.check_date_format(date)
    if False in [is_number, is_date, is_positive]:
      return False
    return True

  def is_positive_number(number):
    if not Validate.is_number(number):
      return "Input Must Be A Number"
    if not Validate.is_positive(number):
      return "Input Must be Positive"
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
  def check_date_format(date):
    # checks for timestamp from API
    if type(date) == float:
      print("check_date_format is float", date)
      return "timestamp"
    print("here: ", date)
    dashes = date.split("-")
    slashes = date.split('/')
    if Validate.check_array_includes_numbers(dashes) and len(dashes[-1]) == 4:
      return "dashes"
    if Validate.check_array_includes_numbers(slashes) and len(slashes[-1]) == 4:
      return "slashes"
    return False

  def check_array_includes_numbers(array):
    if len(array) < 1 or not len(array) == 3:
      return False
    for item in array:
      is_number = Validate.cast_to_number(item)
      if not is_number:
        return False
    return True

  def cast_to_datetime(date_string):
    date_format = Validate.check_date_format(date_string)
    print(date_format)
    if date_format == "dashes":
      return datetime.strptime(date_string, '%d-%m-%Y')
    elif date_format == "slashes":
      return datetime.strptime(date_string, '%d/%m/%Y')
    elif date_format == 'timestamp':
      return datetime.fromtimestamp(date_string)
    else:
      return "Invalid date format"

    
