import requests
from dotenv import load_dotenv
import os
import clui

# Import .env variables
load_dotenv()

# Request Parameters
user_email = os.getenv('USER_EMAIL')
sec_key = os.getenv('ZENDESK_PASSWORD')


def get_data(choice):
    tickets = []
    if int(choice) == 1:
        get_all_tickets()
    elif int(choice) == 2:
        get_one_ticket()
    elif int(choice) == 3:
        print('Thank you and have a nice day. Goodbye.')
    else:
        print("Please enter one of the given choices (1, 2, or 3)")

def get_all_tickets(count):
    # range interation for file name
    for i in range(0, (count - 1)):
        url = "https://d3v-mackroetech.zendesk.com/api/v2/tickets/"+str(i)+".json"
        res = requests.get(url, auth=(user_email, sec_key))
        ticket = res.json()
        # Check for HTTP codes other than 200
        if res.status_code != 200:
            print('Status:', res.status_code, 'Server Unavailable: Attempt Aborted.')
            exit()
        else:
            print(ticket)


def get_one_ticket():
    print("Feature under development")


def main(count):
    clui.display_choices()
    choice = clui.get_input()
    get_data(choice)


main(100)
