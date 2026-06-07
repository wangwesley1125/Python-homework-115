import os

folder = os.path.dirname(os.path.abspath(__file__))
accounts_path = os.path.join(folder, 'accounts.txt')
temp_path = os.path.join(folder, 'temp_file.txt')

accounts = open(accounts_path, 'r')
temp_file = open(temp_path, 'w')

with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if name != 'Doe':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Smith', balance])
            temp_file.write(new_record + '\n')

os.remove(accounts_path)

os.rename(temp_path, accounts_path)