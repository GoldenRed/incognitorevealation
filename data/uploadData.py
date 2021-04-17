import sys, csv, boto3

"""
Uploads data to DynamoDB
"""

if len(sys.argv) < 2:
  raise Exception('Missing TableName Argument!')
table_name = str(sys.argv[1])


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)
try:
  str(table.creation_date_time)
except Exception as e:
  print(e)

with open('data.csv', 'r') as f:
  reader = csv.reader(f, delimiter=';')
  headers = reader.__next__()
  with table.batch_writer() as dbwriter:
    for row in reader:
      dbwriter.put_item(
        Item={
          headers[0] : row[0],
          headers[1] : row[1],
          headers[2] : row[2],
          headers[3] : row[3],
          headers[4] : row[4],
          headers[5] : row[5],
          headers[6] : row[6],
          headers[7] : row[7],
          headers[8] : row[8],
          headers[9] : row[9],
        })
