# ATM Machine
from rich import print, pretty
from rich.progress import track
from rich.table import Table
from rich.console import Console
import pickle
import os
from time import sleep

# Create Object for Balance and Last Transaction
class Account_Info():
    def __init__(self, balance, last_transaction):
        self.balance = balance
        self.last_transaction = last_transaction
    def set_balance(self, balance):
        self.balance = balance
    def add_history(self, action):
        self.last_transaction.append(action)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create Function to save the object
def save_object(obj):
    try:
        with open("data.pickle","wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

# Create Function to load object for next run
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

pin = "123"
pin_answer = input("Please input your pin: ")
# Checks to see if the pin being used to login is correct
if pin == pin_answer:
    # Starts loading bar
    for _ in track(range(100), description='[green]Starting ATM'):
        pretty.install()
        console = Console()
        sleep(0.02)
    special_characters=['!','@','#','$','%','^','&','*','(',')','-','=','+','-']
   # Start of ATM Loop
    while 1: 
        obj = load_object("data.pickle")
        clear_screen()
        console.print("Welcome to the ATM your balance is [bold green]${}[/bold green].".format(obj.balance), style="cyan")
        console.print("Please choose an option from the menu or type \"exit\" to exit.")
        console.print("1. Deposit ")
        console.print("2. Withdraw ")
        console.print("3. View History")
        user_input = input("Input: ")
        if user_input == "1":
            clear_screen()
            console.print("How much would you like to deposit (Number only)")
            deposit = input("Amount to deposit: ")
            # Removes any special characters from answer to avoid exploits/errors
            for i in special_characters:
                checked = deposit.replace(i,"")
            new_balance = obj.balance + int(checked)
            console.print("Your new balance is ${}".format(str(new_balance)))
            # Updates Balance in stored file
            obj.set_balance(new_balance)
            # Adds history to file
            obj.add_history("Deposit {}".format(str(checked)))
            # Saves all updated information to file
            save_object(obj)
            input("Press Enter to go back to main menu.")
        
        elif user_input == "2":
            clear_screen()
            console.print("How much would you like to withdraw? (Number only)")
            withdraw = input("Amount to withdraw: ")
            for i in special_characters:
                checked = withdraw.replace(i,"")
            new_balance = obj.balance - int(checked)
            console.print("Your new balance is ${}".format(str(new_balance)))
            obj.set_balance(new_balance)
            action = "Withdraw {}".format(checked)
            obj.add_history(action)
            save_object(obj)
            input("Press Enter to go back to main menu.")
        
        elif user_input == "3":
            table = Table(title="Previous Transactions oldest to newest:")
            table.add_column("Action", justify="right", style="cyan", no_wrap=True)
            table.add_column("Amount", justify="right", style="green", no_wrap=True)
            last_transactions = obj.last_transaction
            for x in last_transactions: # Breaks format "<ACTION> <AMOUNT> into an array."
                s1 = x.split(" ")[0] 
                s2 = x.split(" ")[1]
                table.add_row(s1, "${}".format(s2)) # Adds row to table for history from array
            console.print(table)
            input("Press Enter to go back to main menu.")
        elif user_input == "exit": # Exit Message
            console.print("Thank you for banking with us.")
            sleep(0.05)
            break
        else:
            print("Type \"exit\" to exit.")
            sleep(0.05)
elif pin != pin_answer:
    print("Wrong Password!")
else:
    print("A Problem Occured.")
