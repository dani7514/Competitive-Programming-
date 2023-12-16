class ATM:
    def __init__(self):
        self.banknotes_count = [0, 0, 0, 0, 0]

    def deposit(self, banknotes_count):
        for i in range(5):
            self.banknotes_count[i] += banknotes_count[i]

    def withdraw(self, amount):
        current_count = self.banknotes_count.copy()
        withdrawal_denominations = [0, 0, 0, 0, 0]

        for i in range(4, -1, -1):
            count_to_withdraw = min(amount // [20, 50, 100, 200, 500][i], current_count[i])
            withdrawal_denominations[i] = count_to_withdraw
            amount -= count_to_withdraw * [20, 50, 100, 200, 500][i]

        if amount == 0:
            for i in range(5):
                self.banknotes_count[i] -= withdrawal_denominations[i]
            return withdrawal_denominations
        else:
            return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)