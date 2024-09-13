
from calculations import minus

import time
import sys

class ATM:
    def __init__(self):
        self.balance = 0

    def set_balance(self, amount):
        self.balance = amount

    def withdraw(self):
        while True:
            try:
                self.withdraw = int(input("How much you want to take"))

                if self.withdraw > self.balance:
                    print("Not enough Balance")

                else:
                    self.balance = minus(self.balance, self.withdraw)

                    print("Please Wait..")
                    for i in range(15):
                        sys.stdout.write("* ")
                        sys.stdout.flush()
                        time.sleep(0.3)

                    print()

                    print("\nPlease take your Amount: GEL {}".format(self.withdraw))
                    print("\nYour balance is: GEL {}".format(self.balance))
                    break
            except Exception as e:
                print("Invalid Input")


a = ATM()
a.set_balance(500)
print(a.withdraw())
