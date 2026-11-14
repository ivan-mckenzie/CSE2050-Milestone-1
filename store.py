from product import Product
from customer import Customer
from order import Order
from order_queue import OrderQueue
from stack import Stack
from hash_mapping import HashMapping
from algorithms import recursive_total_price, fewest_coins, bubble_sort, selection_sort, insertion_sort, binary_search
from algorithms import merge_sort, quick_sort, quick_select

class Store:
    """Class for the store itself that contains customers and products, as well as orders"""
    def __init__(self):
        """Creates a store with empty product and customer lists, as well as a queue for orders that are waiting, an order stack, an order counter, and a hash mapping for product lookup"""
        self.products: list[Product] = []
        self.customers: list[Customer] = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.order_history = Stack()
        self.order_counter = 0
        self.product_map = HashMapping()

    def add_product(self, product: Product):
        """Add a product if its ID is not already stored"""
        if self.find_product(product.get_id()) is not None:
            return False
        else:
            self.products.append(product)
            self.product_map.put(product.get_id(), product)
            return True
        
    def find_product(self, product_id: str):
        """Find and return a product by id using the hash mapping"""
        try:
            return self.product_map.get(product_id)
        except KeyError:
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

    def bubble_sort_products(self):
        """Sorts the store's products by id using bubble sort"""
        bubble_sort(self.products)

    def selection_sort_products(self):
        """Sorts the store's products by id using selection sort"""
        selection_sort(self.products)

    def insertion_sort_products(self):
        """Sorts the store's products by id using insertion sort"""
        insertion_sort(self.products)

    def binary_search_product(self, product_id: str):
        """Finds a product by id with binary search, products must be sorted first"""
        index = binary_search(self.products, product_id)
        if index == -1:
            return None
        return self.products[index]

    def recursive_catalog_total(self):
        """Returns the total price of all products using recursion"""
        return recursive_total_price(self.products)

    def calculate_change(self, coins: list[int], amount: int):
        """Returns the fewest coins needed to make amount"""
        return fewest_coins(coins, amount)

    def merge_sort_products(self):
        """Sorts the store's products by id using merge sort"""
        merge_sort(self.products)

    def quick_sort_products(self):
        """Sorts the store's products by id using quick sort"""
        quick_sort(self.products)

    def quick_select_product(self, k: int):
        """Returns the product at rank k by id, where k = 0 is the smallest"""
        return quick_select(self.products, k)