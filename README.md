<h2 align="center"> Cloud Engineer Tech Exercise </h2>
 <p align="center">  <a href='#overview'>Overview</a> |  <a href='#requirements'>Requirements</a>   |   <a href='#versions'>Versions</a> |   <a href='#example'>Example</a> |  <a href='#links'>Useful Links</a> 

## Python Bank App
### Overview <a name="overview"> </a>
Create a bank app which satisfies the following acceptance criteria:
```
Given a client makes a deposit of 1000 on 10-01-2012
And a deposit of 2000 on 13-01-2012
And a withdrawal of 500 on 14-01-2012
When she prints her bank statement
Then she would see
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```

### Requirements <a name="requirements"> </a>
You should be able to interact with your code via python console.
Deposits, withdrawal can be taken in as inputs to the python script
Account statement (date, amount, balance) printed on the console.
Your code should follow SOLID principles 

### Versions <a name="versions"> </a>
#### Version 1 
- Data can be kept in memory (it doesn't need to be stored to a database or anything).
- Good documentation
- Code at a place where we can access it from

#### Version 2
- Add unit tests to validate your code
- Push the data to a database (like dynamoDB on AWS)

#### Version 3
- Think of Infrastructure as code for your resources
- Run this as a Serverless app with an api to access this 

### Example for a interactive python code is in the repo <a name="example"> </a>

Assuming your code looks like this:

```
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        [...]
```

We would want to interact with it like this:

```
$ python
Python 3.6.7 (default, Nov 26 2018, 15:05:20) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bank = Bank(100)
>>> bank.deposit(50)
```

*Note: This is only for illustrating how you can have an interactive python console. Please feel free to use different names for Classes/objects/functions* 

### Some of the tools we use <a name="links"> </a>
- AWS https://aws.amazon.com/  (EC2, S3, RDS, Lambda, DynamoDB)
- Cloudformation https://aws.amazon.com/cloudformation/
- Python https://www.python.org/
- Docker https://www.docker.com/
- Ansible http://docs.ansible.com/
- Serverless https://serverless.com/

Notes: 
- Make sure we can access your repo. 
- You will have the opportunity to tell us about your reasoning, process and choice of tools during your interview. We are as interested in what you’ve built as we are in how you built it and why!

Good luck!
