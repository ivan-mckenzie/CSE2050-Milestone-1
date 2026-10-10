from customer import Customer
from product import Product

class Order:
    '''order class'''
    def __init__(self, order_id: str, customer: Customer, items: list[Product]):
        '''order init function'''
        self.order_id = order_id
        self.customer = customer
        self.items = list(items)
        self.status = "PENDING"

    def get_id(self):
        '''returns order id'''
        return self.order_id

    def get_customer(self):
        '''returns customer'''
        return self.customer

    def get_items(self):
        '''returns items list of the order'''
        return self.items

    def get_status(self):
        '''returns status of the order'''
        return self.status

    def set_status(self, status: str):
        '''changes the order status'''
        self.status = status

    def calculate_total(self):
        '''returns order total'''
        total = 0
        for i in self.items:
            total += i.get_price()

        return total

        