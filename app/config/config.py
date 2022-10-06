import configparser

# read configs
parser = configparser.ConfigParser()
parser.read('./app/config/config.ini')

aws_access_key_id = parser.get('dynamodb', 'aws_access_key_id')
aws_secret_access_key = parser.get('dynamodb', 'aws_secret_access_key')
region_name = parser.get('dynamodb', 'region_name')
db_table = parser.get('dynamodb', 'table')