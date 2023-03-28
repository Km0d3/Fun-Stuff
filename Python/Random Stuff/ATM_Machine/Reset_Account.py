import pickle

class Account_Info():
    def __init__(self, balance, last_transaction):
        self.balance = balance
        self.last_transaction = last_transaction
    def set_balance(self, balance):
        self.balance = balance
    def add_history(self, action):
        self.last_transaction.append(action)

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

obj = Account_Info(0, [])
save_object(obj)