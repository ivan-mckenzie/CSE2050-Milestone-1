from product import Product
from customer import Customer

class Store:
    """Class for the store itself that contains customers and products"""
    def __init__(self):
        """Creates a store with empty product and customer lists"""
        self.products: list[Product] = []
        self.customers: list[Customer] = []

    def add_product(self, product: Product):
        """Add a product if its ID is not already stored"""
        if self.find_product(product.get_id()) is not None:
            return False
        else:
            self.products.append(product)
            return True
        
    def find_product(self, product_id: str):
        """Find and return a product by id"""
        for product in self.products:
            if product.get_id() == product_id:
                return product
            else:
                return None
            
    def add_customer(self, customer: Customer):
        if self.find_customer(customer.get_id()) is not None:
            return False
        else:
            self.customers.append(customer)
            return True
        
    def find_customer(self, customer_id: str):
        """Find and return a customer by id"""
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer
            else:
                return None