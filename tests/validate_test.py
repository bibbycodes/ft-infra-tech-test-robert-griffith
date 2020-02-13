from lib.Validate import Validate
from datetime import datetime

def test_is_number_with_zero():
  assert Validate.is_number(0) == True

def test_is_number_with_one():
  assert Validate.is_number(1) == True

def test_is_number_with_float():
  assert Validate.is_number(1.0) == True

def test_is_number_with_string_representation():
  assert Validate.is_number("0") == True

def test_is_number_with_empty_string():
  assert Validate.is_number("") == False

def test_is_number_with_string():
  assert Validate.is_number("hello") == False

def test_is_positive_with_zero_string():
  assert Validate.is_positive("0") == False

def test_is_positive_with_empty_string():
  assert Validate.is_positive("") == False

def test_is_positive_with_negative_string():
  assert Validate.is_positive("-1") == False

def test_is_positive_with_integer():
  assert Validate.is_positive(1) == True

def test_is_positive_with_float():
  assert Validate.is_positive(1.0) == True

def test_is_positive_with_string():
  assert Validate.is_positive("hello") == False

def test_check_date_format_with_slashes():
  assert Validate.check_date_format("10/10/2020") == "slashes"

def test_check_date_format_with_dashes():
  assert Validate.check_date_format("10-10-2020") == "dashes"

def test_cast_to_datetime_with_valid_input_slashes():
  date = Validate.cast_to_datetime("10/10/2020")
  assert isinstance(date, datetime)

def test_cast_to_datetime_with_valid_input_dashes():
  date = Validate.cast_to_datetime("10-10-2020")
  assert isinstance(date, datetime)

def test_cast_to_datetime_with_invalid_input_slashes():
  date = Validate.cast_to_datetime("10/102020")
  assert date == "Invalid date format"

def test_cast_to_datetime_with_invalid_input_dashes():
  date = Validate.cast_to_datetime("1010-2020")
  assert date == "Invalid date format"
