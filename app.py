import os
import boto3
from lib.Account import Account
from lib.Statement import Statement
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  account = Account()
  account.deposit(500)
  account.deposit(500)
  account.withdraw(600)
  statement = Statement.make(account)
  return statement