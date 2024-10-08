class BankAccount:
    def __init__(self, transaction_history = []):
        self.balance = 0
        self.transaction_history = transaction_history

        for transaction in transaction_history:
            self.balance += transaction['amount']

    def deposit(self, transaction):
        if transaction['type'] == 'd':
            self.balance += transaction['amount']
            self.transaction_history.append(transaction)


    def withdraw(self, transaction):
        if transaction['type'] == 'w':
            self.balance -= transaction['amount']
            self.transaction_history.append(transaction)

    def __str__(self):
        return f"Balance : {self.balance}, Transactions : {self.transaction_history}"

checking_transaction_history = [
    {"dt": 0, "type": "d", "amount": 100},
    {"dt": 1, "type": "w", "amount": 53},
    {"dt": 4, "type": "w", "amount": 12},
    {"dt": 2, "type": "d", "amount": 350},
    {"dt": 3, "type": "w", "amount": 576},
    {"dt": 7, "type": "w", "amount": 295},
    {"dt": 10, "type": "d", "amount": 1010},
]

savings_transaction_history = [
    {"dt": 0, "type": "d", "amount": 150},
    {"dt": 1, "type": "d", "amount": 25},
    {"dt": 5, "type": "d", "amount": 100},
    {"dt": 2, "type": "w", "amount": 10},
    {"dt": 8, "type": "w", "amount": 200},
]    

sorted(checking_transaction_history, key = lambda x :x['dt']  )
sorted(savings_transaction_history, key = lambda x :x['dt']  )

checking_account = BankAccount(transaction_history=checking_transaction_history)
savings_account = BankAccount(transaction_history=savings_transaction_history)

for transaction in checking_transaction_history:
    if transaction['type'] == 'd':
        checking_account.deposit(transaction)
    elif transaction['type'] == 'w':
        checking_account.withdraw(transaction)


for transaction in savings_transaction_history:
    if transaction['type'] == 'd':
        savings_account.deposit(transaction)
    elif transaction['type'] == 'w':
        savings_account.withdraw(transaction)

print(checking_account)
print("\n")

print("Savings Account: \n", savings_account)