import requests
from dotenv import load_dotenv

# Import .env variables
load_dotenv()

# Parameters
url = 'https://d3v-mackroetech.zendesk.com'
user_email = USER_EMAIL
sec_key = ZENDESK_PASSWORD


r = requests.get(url, params = PARAMS)

data = r.json()
