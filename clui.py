# Commang Line User Interface

# TODO: Import retrieved data from tickets.py to display?

# class CLUI:
#     def __init__(self):
#         pass

def display_choices():
    print("")
    print("*** Zendesk Ticket Viewer ***")
    print("")
    print("Choice 1: View All Tickets (Enter: 1)")
    print("Choice 2: View One Ticket (Enter: 2)")
    print("Choice 3: Exit (Enter: 3)")

def get_input():
    user_action_choice = input("Please enter your choice: ")
    return int(user_action_choice)

def display_output(self):
    pass
