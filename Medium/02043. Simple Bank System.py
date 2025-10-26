class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.n = len(balance)
        
    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        # Validate both accounts exist and account1 has sufficient balance
        if (account1 < 1 or account1 > self.n or 
            account2 < 1 or account2 > self.n or 
            self.balance[account1 - 1] < money):
            return False
        
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
        
    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Validate account exists
        if account < 1 or account > self.n:
            return False
        
        # Perform deposit
        self.balance[account - 1] += money
        return True
        
    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Validate account exists and has sufficient balance
        if (account < 1 or account > self.n or 
            self.balance[account - 1] < money):
            return False
        
        # Perform withdrawal
        self.balance[account - 1] -= money
        return True
