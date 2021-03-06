import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    try:
        with open(client_filename, 'a') as fi:
            fi.write(str(client_name) + '\n')
        print('Client added: ' + client_name)

    except:
        print('Error: Client not added')

def add_transaction(debtor, creditor, amount):
    dca = str(debtor) + ", " + str(creditor) + ", " + str(amount) + "\n"
    with open("transactions.txt", "a") as f:
    	f.write(dca)
    return ":)"
        

def get_clients():
    return(list(map(lambda x:x.strip(), open(client_filename,'r').readlines())))

def get_transactions():
    with open("transactions.txt", "r") as f:
        trans = list(map(lambda x: x.strip().split(), f.readlines()))
    return trans

