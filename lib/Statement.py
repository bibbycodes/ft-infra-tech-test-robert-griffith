class Statement:
  def headers():
    return 'date || credit || debit || balance \n'

  def format_transaction(transaction, account):
    items = Statement.format_items(transaction, account)
    if transaction.transaction_type == "deposit":
      return "{} || {} || || {} \n".format(items[0], items[1], items[2])
    return "{} || || {} || {} \n".format(items[0], items[1], items[2])

  def format_items(transaction, account):
    date = transaction.date.strftime("%d/%m/%Y")
    amount = ('%.2f' % transaction.amount)
    balance = ('%.2f' % account.balance)
    return [date, amount, balance]

  def make(account):
    headers = Statement.headers()
    output_string = ""
    for record in account.ledger:
      # record[0] => transaction, record[1] => current_balance
      output_string += Statement.format_transaction(record[0], account)
    return headers + output_string
