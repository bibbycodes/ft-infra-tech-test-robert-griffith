import boto3

def sort_transactions_by_timestamp(transactions):
  return sorted(transactions, key = lambda i: float(i['timestamp']['S']), reverse=True)

def setup_db(IS_OFFLINE):
  if IS_OFFLINE:
    client = boto3.client(
      'dynamodb',
      region_name='localhost',
      endpoint_url='http://localhost:8000'
    )
  else:
    client = boto3.client('dynamodb')
  return client