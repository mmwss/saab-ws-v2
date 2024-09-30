"""
Fix the race condition in a multi-threaded program
that simulates transfers between bank accounts.
Implement a solution that ensures thread safety
without removing the sleep statements.
"""

import threading
import time
import random

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # Simulate delay to force race condition
        temp = self.balance
        time.sleep(random.uniform(0.001, 0.01))
        temp += amount
        self.balance = temp

    def withdraw(self, amount):
        if self.balance >= amount:
            # Simulate delay to force race condition
            temp = self.balance
            time.sleep(random.uniform(0.001, 0.01))
            temp -= amount
            self.balance = temp
            return True
        return False

def transfer(from_account, to_account, amount):
    if from_account.withdraw(amount):
        time.sleep(random.uniform(0.001, 0.01))
        to_account.deposit(amount)

# Example usage
if __name__ == "__main__":
    acc1 = BankAccount("Account A", 1000)
    acc2 = BankAccount("Account B", 1000)

    threads = []

    for _ in range(100):
        t1 = threading.Thread(target=transfer, args=(acc1, acc2, 5))
        t2 = threading.Thread(target=transfer, args=(acc2, acc1, 5))
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()

    for t in threads:
        t.join()

    print(f"{acc1.name} Final Balance: {acc1.balance}")
    print(f"{acc2.name} Final Balance: {acc2.balance}")
    print(f"Total: {acc1.balance + acc2.balance} (should be 2000)")
