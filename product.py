class Product:
    """Stores an item sold by the store"""
    def __init__(self, product_id: str, name: str, price:float):
        """Creates a product with a given id, name, and price"""
        self.product_id = product_id
        self.name = name
        self.price = price
    def get_id(self):
        """Returns a product's id"""
        return self.product_id
    def get_name(self):
        """Returns a product's name"""
        return self.name
    def get_price(self):
        """Returns a product's price as a float"""
        return self.price
    