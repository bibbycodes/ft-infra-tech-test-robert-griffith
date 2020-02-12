class Statement:
  def make_headers():
    return 'date || credit || debit || balance \n'

  def format_transaction(transaction, account):
    date = transaction.date.strftime("%d/%m/%Y")
    amount = ('%.2f' % transaction.amount)
    balance = ('%.2f' % account.balance)
    if transaction.transaction_type == "deposit":
      return "{} || {} || || {} \n".format(date, amount, balance)
    return "{} || || {} || {} \n".format(date, amount, balance)
