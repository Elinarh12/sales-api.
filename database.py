import pandas as pd

class Database:

    def __init__(self):
        self.orders = pd.read_csv("/storage/emulated/0/orders.csv")
        self.users = pd.read_csv("/storage/emulated/0/users.csv")

    def get_orders(self):
        return self.orders

    def get_users(self):
        return self.users