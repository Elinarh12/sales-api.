from database import Database

class SalesService:

    def __init__(self):
        self.db = Database()

    def sales_by_city(self):
        orders = self.db.get_orders()

        return (
            orders.groupby("city")["price"]
            .sum()
            .to_dict()
        )

    def top_customers(self):
        orders = self.db.get_orders()

        return (
            orders.groupby("customer_id")["price"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .to_dict()
        )

    def stats(self):
        orders = self.db.get_orders()

        return orders["price"].describe().to_dict()