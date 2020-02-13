# record[0] => transaction, record[1] => current_balance
from datetime import datetime

class Statement:
  def headers():
    return 'date || credit || debit || balance\n'

  def format_transaction(record):
    items = Statement.format_items(record)
    if record[0].transaction_type == "deposit":
      return "{} || {} || || {}\n".format(items[0], items[1], items[2])
    elif record[0].transaction_type == "withdraw":
      return "{} || || {} || {}\n".format(items[0], items[1], items[2])
    return "Invalid Transaction Type"

  def format_items(record):
    date = record[0].date
    print(type(date))
    if type(date) == float:
      date = datetime.fromtimestamp(date)
    date = date.strftime("%d/%m/%Y")
    amount = ('%.2f' % abs(record[0].amount))
    balance = ('%.2f' % record[1])
    return [date, amount, balance]

  def make(account):
    headers = Statement.headers()
    output_string = ""
    for record in account.ledger:
      output_string += Statement.format_transaction(record)
    return (headers + output_string)[:-1] # removes final \n
