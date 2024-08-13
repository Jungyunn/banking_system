class Account:
    def __init__(self, account_id, balance, customer_name):
        self.account_id = account_id
        self.balance = balance
        self.customer_name = customer_name
    
    def get_account_id(self):
        return self.account_id

    def deposit():
        pass
    
    def withdraw():
        pass

    def show_account_information(self):
        print("계좌ID:", self.account_id)
        print("이름:", self.customer_name)
        print("잔액:", self.balance)
    