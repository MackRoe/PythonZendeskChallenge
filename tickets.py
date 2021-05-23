import requests
from dotenv import load_dotenv
import clui

# Import .env variables
load_dotenv()

# Request Parameters
url = 'https://d3v-mackroetech.zendesk.com/api/v2/' + endpoint_filename
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

def get_data(choice):
    if choice = 1:
        get_all_tickets()
        for ticket in tickets:
            for attribute in attributes:
                print('Attribute:' ticket.attribute)
    elif choice == 2:
        get_one_ticket()
    elif choice == 3:
        print('Thank you and have a nice day. Goodbye.')
    else:
        print("Please enter one of the given choices (1, 2, or 3)")

def get_all_tickets:
    pass

def get_one_ticket:
    pass
