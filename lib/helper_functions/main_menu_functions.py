from helper_functions.browse_store_functions import *
from helper_functions.buy_checkout_functions import *
from helper_functions.sell_functions import *
from helper_functions.view_account import *

def main_menu(shopper):
    def prompt2():
        print("\nWhat can we help you with today?")
        print("1. Browse Store")
        print("2. Buy Items")
        print("3. Sell Items")
        print("4. Chat")
        print("5. View your account")
        print("6. Leave Store")

    while True:
        prompt2()
        curr_shopper = Shopper.find_by_id(shopper.id)
        print("Shopper from main menu: PAY ATTENTION HERE")
        print(curr_shopper)
        print(curr_shopper.user_name)
        choice_2 = input("> ")
        if choice_2 == "1":
            browse_store()
        elif choice_2 == "2":
            buy_from_store()
        elif choice_2 == "3":
            sell_game(curr_shopper) 
        elif choice_2 == "4":
            print("Will show chatting prompt and will prompt questions for store attendee?\n")
        elif choice_2 == "5":
            get_account(curr_shopper)
        elif choice_2 == "6":
            exit_program()
        else:
            print(f"{choice_2} is not a valid input. Please enter a number 1-5.\n")