from flask import Flask, jsonify
from Service import SalesService

class SalesAPI:

    def __init__(self):
        self.app = Flask(__name__)
        self.Service = SalesService()

        self.register_routes()

    def register_routes(self):

        @self.app.route("/")
        def home():
            return jsonify({"message": "Sales API Running"})

        @self.app.route("/sales/by-city")
        def by_city():
            return jsonify(
                self.Service.sales_by_city()
            )

        @self.app.route("/sales/top-customers")
        def top_customers():
            return jsonify(
                self.Service.top_customers()
            )

        @self.app.route("/sales/stats")
        def stats():
            return jsonify(
                self.Service.stats()
            )

    def get_app(self):
        return self.app