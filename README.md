<div align="center">
<img src="https://travis-ci.com/bibbycodes/ft-infra-tech-test-robert-griffith.svg?token=GtuEshpCkADdwz3Mtzd1&branch=master">
</div>

<h1 align=center>Robert Griffith - FT Cloud Engineer Tech Test Solution</h1>

<div align="center">

[Usage ](#usage) |
[Process ](#process) |
[Architecture ](#architecture)|
[Challenges ](#challenges) |
[Technologies ](#technologies) |
[What I Learned ](#what)|
[Extending](#extending)

</div>

## Usage

To use this code you must have an AWS account and credentials must be supplied. To check if you have credentials stored on your computer type in the following command into the terminal.

`nano ~/.aws/credentials`

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
