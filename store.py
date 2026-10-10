from product import Product
from customer import Customer
from order import Order
from order_queue import OrderQueue
from stack import Stack

class Store:
    """Class for the store itself that contains customers and products, as well as orders"""
    def __init__(self):
        """Creates a store with empty product and customer lists, as well as a queue for orders that are waiting, an order stack, and an order counter"""
        self.products: list[Product] = []
        self.customers: list[Customer] = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.order_history = Stack()
        self.order_counter = 0

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
        return None
            
    def add_customer(self, customer: Customer):
        """Adds a customer"""
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
        return None
    def find_order(self, order_id):
        """Find and return an order by id, return None if not found"""
        for order in self.orders:
            if order.get_id() == order_id:
                return order
        return None
    def get_orders(self):
        """Returns a list of all orders"""
        return self.orders
    def checkout(self, customer_id):
        """Creates an order from the cart, stores it in the orders, queues it, and gets rid of items in the cart. Returns None if cart is empty."""
        customer = self.find_customer(customer_id)
        if customer is None:
            return None

        cart = customer.get_cart()
        if cart.is_empty():
            return None

        self.order_counter += 1
        order = Order("O" + str(self.order_counter), customer, cart.get_items() )
        self.orders.append(order)
        self.order_queue.enqueue(order)
        cart.clear()
        return order

    def process_next_order(self):
        """Removed oldest order, sets it as processing, and saves it to history. Returns none if no orders in queue"""
        order = self.order_queue.dequeue()
        if order is None:
            return None
        order.set_status("PROCESSING")
        self.order_history.push(order)
        return order
    def get_order_history(self):
        """Returns processed orders from most recent to oldest"""
        orders = []
        node = self.order_history.LL._head
        while node is not None:
            orders.append(node.item)
            node = node.link
        return orders

    