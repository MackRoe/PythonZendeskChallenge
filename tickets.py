import requests
from dotenv import load_dotenv
import os
from pprint import pprint
import clui
import array_helper

# Import .env variables
load_dotenv()

# Request Parameters
user_email = os.getenv('USER_EMAIL')
sec_key = os.getenv('ZENDESK_PASSWORD')
base_url = os.getenv('ZENDESK_URL')


def get_data(choice, count):
    ''' Handle user choice to retrieve data '''
    tickets = []
    if int(choice) == 1:
        get_all_tickets(count)
    elif int(choice) == 2:
        ticket_number = clui.get_ticket_number()
        get_one_ticket(ticket_number)
    elif int(choice) == 3:
        print('Thank you and have a nice day. Goodbye.')
    else:
        print("Please enter one of the given choices (1, 2, or 3)")

def get_all_tickets(count):
    ''' Get all the tickets from the Zendesk API '''
    # build a comma seperated value string
    ids = array_helper.make_array()

    # build the request url
    url = base_url + "1"
    # make the request
    res = requests.get(url, auth=(user_email, sec_key))
    print(res.content)
    # Decode JSON into dictionary
    tickets = res.json()
    print('')
    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Server Unavailable: Attempt Aborted.')
        exit()
    else:
        for i in range(1, 100):
            # build request url
            url = base_url + str(i)
            # GET record from API
            res = requests.get(url, auth=(user_email, sec_key))
            # Decode JSON into python dict
            data = res.json()
            for dat in data:
                print('--------------')
                print('*** TICKET', i, '***')
                pprint(data)


                # ** Print Statements Commented Out for Debug **
                # print("Ticket Subject: ", ticket['subject'])
                # print("Created at ", ticket['created_at'])
                # print("By User", ticket['submitter_id'])
                # print("Status: ", ticket['status'])
                print('--------------')
                # print('')


def get_one_ticket(ticket_number):
    ''' Get one ticket from the Zendesk API '''
    # build request url
    url = base_url + str(ticket_number)
    # GET record from API
    res = requests.get(url, auth=(user_email, sec_key))
    # Decode JSON into python dict
    ticket = res.json()
    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Server Unavailable: Attempt Aborted.')
        exit()
    else:
        print('--------------')
        print('*** TICKET DATA ***')
        pprint(ticket)
        print('--------------')

        # ** Print Statements Commented Out for Debug **
        # print("Ticket Subject: ", ticket['subject'])
        # print("Created at ", ticket['ticket.created_at'])
        # print("By User", ticket['submitter_id'])
        # print("Status: ", ticket['status'])
        # print('')


def main(count):
    ''' Function calls to run the program '''
    clui.display_choices()
    choice = clui.get_input()
    get_data(choice, count)

# Runs Program
if __name__ == "__main__":
    main(100)
