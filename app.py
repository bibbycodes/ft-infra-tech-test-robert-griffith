import os
import boto3
from lib.Account import Account
from lib.Statement import Statement
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)
TRANSACTIONS_TABLE = os.environ['TRANSACTIONS_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

#switch db depending on envirnment
if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')

@app.route('/')
def home():
  print("Statement")
  account = Account()
  account.deposit(500)
  account.deposit(500)
  account.withdraw(600)
  statement = Statement.make(account)
  return statement

# find by transaction id
@app.route('/transactions/all')
def data():
  result = client.scan(
    TableName=TRANSACTIONS_TABLE,
    Select='ALL_ATTRIBUTES'
  )
  return result
  # res = client.get_item(
  #   TableName=TRANSACTIONS_TABLE,
  #   Key={
  #     'transactionDate': {'S', transaction_date }
  #   }
  # )
  # transaction = res.get('Item')
  # print(transaction)
  # if not transaction:
  #   return jsonify({'error: Not Found'}), 404

  # return jsonify({
  #   'transactionId'     : transaction.get('transactionId'),
  #   'transactionType'   : transaction.get('transactionType').get('S'),
  #   'transactionAmount' : transaction.get('transactionAmount'),
  #   'accountBalance'    : transaction.get('accountBalance'),
  #   'transactionDate'   : transaction.get('transactionDate')
  # })

# withdraw / deposit should only have amount and type in request
@app.route('/transactions/add', methods=["POST"])
def add_transaction():
  transaction_id = str(uuid.uuid4())
  transaction_type = request.json.get('transactionType')
  transaction_date = request.json.get('transactionDate')
  transaction_amount = str(request.json.get('transactionAmount'))
  account_balance = str(request.json.get('accountBalance'))

  response = client.put_item(
    TableName=TRANSACTIONS_TABLE,
    Item={
      'transactionId'     : {'S' : transaction_id},
      'transactionType'   : {'S' : transaction_type},
      'transactionAmount' : {'N' : transaction_amount},
      'accountBalance'    : {'N' : account_balance},
      'transactionDate'   : {'S' : transaction_date}
    }
  )

  return jsonify({
    'transactionType'   : transaction_type,
    'transactionAmount' : transaction_amount,
    'accountBalance'    : account_balance,
    'transactionDate'   : transaction_date
  })