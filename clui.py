# Commang Line User Interface
# clui.py

def display_choices():
    ''' Displays the choices available to the user '''
    print("")
    print("*** Zendesk Ticket Viewer ***")
    print("")
    print("Choice 1: View All Tickets (Enter: 1)")
    print("Choice 2: View One Ticket (Enter: 2)")
    print("Choice 3: Exit (Enter: 3)")

def get_input():
    ''' Gets the user choice from the terminal '''
    user_action_choice = input("Please enter your choice: ")
    return int(user_action_choice)

def get_ticket_number():
    ticket_number = input("Please enter the number of the ticket you wish to view: ")
    return int(ticket_number)
