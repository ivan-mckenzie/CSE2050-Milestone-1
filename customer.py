from cart import ShoppingCart

class Customer:
    """creates a customer object"""
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self) -> str:
        """gets the customer id"""
        return self.customer_id

    def get_name(self) -> str:
        """gets the customer name"""
        return self.name

    def get_cart(self) -> ShoppingCart:
        """gets the customer cart"""
        return self.cart
    