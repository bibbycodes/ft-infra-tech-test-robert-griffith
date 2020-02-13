import os
import boto3
from lib.Account import Account
from lib.Statement import Statement
from flask import Flask, jsonify, request
from time import time
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
def all_transactions():
  result = client.scan(
    TableName=TRANSACTIONS_TABLE,
    Select='ALL_ATTRIBUTES'
  )
  transactions = result.get('Items')
  #sort results by timestamp
  sorted_transactions = sort_transactions_by_timestamp(transactions)
  return jsonify(sorted_transactions)

@app.route('/statement')
def statement():
  account = Account()
  result = client.scan(
    TableName=TRANSACTIONS_TABLE,
    Select='ALL_ATTRIBUTES'
  )
  transactions = result.get('Items')
  sorted_transactions = sort_transactions_by_timestamp(transactions)

  return jsonify(transactions)

@app.route('/transactions/add', methods=["POST"])
def add_transaction():
  transaction_id = str(uuid.uuid4())
  transaction_type = request.json.get('transactionType')
  timestamp =  str(int(time() * 1000))
  transaction_amount = request.json.get('transactionAmount')
  account_balance = request.json.get('accountBalance')

  response = client.put_item(
    TableName=TRANSACTIONS_TABLE,
    Item={
      'transactionId'     : {'S' : transaction_id},
      'transactionType'   : {'S' : transaction_type},
      'transactionAmount' : {'N' : transaction_amount},
      'accountBalance'    : {'N' : account_balance},
      'timestamp'         : {'S' : timestamp}
    }
  )

  return jsonify({
    'transactionType'   : transaction_type,
    'transactionAmount' : transaction_amount,
    'accountBalance'    : account_balance,
    'timestamp'         : timestamp
  })

def sort_transactions_by_timestamp(transactions):
  return (sorted(transactions, key = lambda i: int(i['timestamp']['S'])))