import json

class Api:

    database = None

    def __init__(self, database):
        self.database = database


    def get_products(self, f={}):
        products = self.database.get_products(f)
        return json.dumps({'products': products})


    def add_product(self, product):
        pass


    def sell_products(self, products, from_acc, to_acc):
        pass


    def buy_products(self, products, from_acc, to_acc):
        pass


    def update_product(self, product):
        pass

    def make_transaction(self, products, from_acc, to_acc):
        pass


    def get_transactions(self, f={}):
        pass


    def add_account(self, account):
        pass


    def get_accounts(self, f={}):
        pass


    def add_location(self, location):
        pass


    def get_locations(self, f={}):
        pass


    def get_stock(self, products=None, location=None):
        pass

    def set_stock(self, products, location):
        pass

    def move_products(self, product, l_from, l_to):
        pass


