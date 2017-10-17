import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    pass
      
def add_transaction(debtor, creditor, amount):
    dca = str(debtor) + ", " + str(creditor) + ", " + str(amount) + "\n"
    with open("transactions.txt", "a") as f:
    	f.write(dca)
    return ":)"
        
def get_clients():
    pass

def get_transactions():
    with open("transactions.txt", "r") as f:
        trans = list(map(lambda x: x.strip().split(), f.readlines()))
    return trans
