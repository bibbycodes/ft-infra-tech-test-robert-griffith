<div align="center">
<img src="https://travis-ci.com/bibbycodes/ft-infra-tech-test-robert-griffith.svg?token=GtuEshpCkADdwz3Mtzd1&branch=master">
</div>

<h1 align=center>Robert Griffith - FT Cloud Engineer Tech Test Solution</h1>

<div align="center">

[Setup ](#setup) |
[Usage ](#usage) |
[Process ](#process) |
[Architecture ](#architecture)|
[Challenges ](#challenges) |
[Technologies ](#technologies) |
[What I Learned ](#what)|
[Extending](#extending)

</div>

## Setup
To fully use this code you must have an AWS account and credentials must be supplied. To check if you have credentials stored on your computer type in the following command into the terminal.
`cat ~/.aws/credentials`

If the credentials are not present, make sure you set up an AIM user and save your credentials in the following format:

```shell
[default]
aws_access_key_id = <YOUR_ACCESS_KEY>
aws_secret_access_key = <YOUR_SECRET_KEY>
```

Next you should clone this repo and change into the resulting directory.
Now you can start installing packages and setting up the virtual environment.

`npm install` <br>
`pip install -r requirements.txt` <br>

You must also install the sdynamoDB locally:
`sls dynamodb install`

#### Running The Api Locally
To run the app locally you will need two terminals. In the first terminal enter:
`sls dynamodb start`

In the second terminal enter:
`sls wsgi server`

You should now be able to visit `http://localhost:5000` and access the API.

#### Deploying to AWS
In order to deply to AWS you simply type in the following command:
`sls deploy`

This will deploy the database and static files to aws and provide you with a URL endpoint from which you can access the API.

## Usage
First activate the virtual environment and enter the python REPL:
```shell
(venv) (base) $>> source venv/bin/activate`
(venv) (base) $>> python
Python 3.7.4 (default, Aug 13 2019, 15:17:50) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
From here you can import the models and start interacting.
```shell
>>> from lib.Statement import Statement
>>> from lib.Account import Account
>>> my_account = Account(1000)
>>> my_account.balance
1000.0
```
Here we have made an account object and initialzed it a starting balance of 1000. If the starting balance is not supplied, the account will be initialzed with a balance of 0.
Every time we deposit or withdraw money from the account the balance is updated
```shell
>>> my_account.add_transaction("deposit", 1000)
<lib.Transaction.Transaction object at 0x10b66e210>
>>> my_account.add_transaction("withdraw", 500)
<lib.Transaction.Transaction object at 0x10b66e810>
>>> my_account.balance
1500.0
```
If we want to print a statement, we simply pass the account object to the statement class and print it.
```shell
>>> print(Statement.make(my_account))
date || credit || debit || balance
14/02/2020 || 1000.00 || || 2000.00
14/02/2020 || || 500.00 || 1500.00
```
`add_transaction` also accepts a third optional argument that specifies the transaction date. If this argument is not supplied, then the transaction date is set to today. The transaction date argument can be supplied in the format of dd/mm/yyy, dd-mm-yyyy or as an epoch timestamp.
```shell
>>> my_account.add_transaction("withdraw", 700, '10-10-2020')
>>> my_account.add_transaction("deposit", 800, '10-10-2020')
<lib.Transaction.Transaction object at 0x10b65fad0>
>>> print(Statement.make(my_account))
14/02/2020 || 1000.00 || || 2000.00
14/02/2020 || || 500.00 || 1500.00
10/10/2020 || || 700.00 || 800.00
15/10/2020 || 800.00 || || 1600.00
```

Please note that when supplying dates for each transaction it is assumed that these are added in order.

#### API
The API portion of this solution represents a single account. You can deposit and withdraw money as well as get a json file of all transaction and have a statement returned through the following 3 endpoints:

`POST /transactions/add`<br>
`GET /transactions/all`<br>
`GET /statement`

When adding transactions you must supply the transaction type and amount.

## Process
