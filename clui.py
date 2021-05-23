# Commang Line User Interface

class CLUI:
    def __init__(self):
        pass

    def display_choices(self):
        print("Choice 1: View All Tickets (Enter: 1)")
        print("Choice 2: View One Ticket (Enter: 2)")
        print("Choice 3: Exit (Enter: 3)")

    def get_input(self):
        user_action_choice = input("Please enter your choice")
        return user_action_choice

    def return_output(self):
        pass
