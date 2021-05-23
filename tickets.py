import requests
from dotenv import load_dotenv

# Import .env variables
load_dotenv()

# Request Parameters
url = 'https://d3v-mackroetech.zendesk.com/api/v2/'
user_email = USER_EMAIL
sec_key = ZENDESK_PASSWORD

endpoint_filename = ''

# HTTP get request
res = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200;
    print('Status:', response.status_code, 'Unsuccessful Page Load: Aborted.')
    exit()

# JSON response convert to dictionary
data = res.json()
