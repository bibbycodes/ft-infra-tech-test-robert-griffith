import os
from lib.Account import Account
from lib.helpers import *
from lib.Statement import Statement
from flask import Flask, jsonify, request
from time import time
import uuid

app = Flask(__name__)
TRANSACTIONS_TABLE = os.environ['TRANSACTIONS_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

client = setup_db(IS_OFFLINE)

@app.route('/')
def home():
  return "FT TECH TEST - ROBERT GRIFFITH"

@app.route('/transactions/all')
def all_transactions():
  result = client.scan(
    TableName=TRANSACTIONS_TABLE,
    Select='ALL_ATTRIBUTES'
  )
  transactions = result.get('Items')
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
  for record in sorted_transactions:
    account.add_transaction(
      record["transactionType"]['S'],
      float(record["transactionAmount"]['N']),
      float(record["timestamp"]['S'])
    )
  statement = Statement.make(account)
  return statement

@app.route('/transactions/add', methods=["POST"])
def add_transaction():
  transaction_type = request.json.get('transactionType')
  # boto3 rejects int types on insertion
  transaction_id = str(uuid.uuid4())
  timestamp =  str(time())
  account_balance = str(request.json.get('accountBalance'))
  transaction_amount = str(request.json.get('transactionAmount'))

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

