from product import Product

class ShoppingCart:
    """the shopping cart class which holds products"""
    def __init__(self):
        self.items: list[Product] = []


    def add_product(self, product: Product) -> None:
        """adds product to shopping cart"""
        self.items.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Removes the product from the cart"""
        for product in self.items:
            if product.get_name() == product_id:
                self.items.remove(product)
                return True
        return False

    def get_items(self) -> list[Product]:
        """returns items in cart"""
        return self.items

    def calculate_total(self) -> float:
        """returns the sum of product prices in the cart"""
        total = 0
        for product in self.items:
            total += product.get_price()

        return total

    def is_empty(self) -> bool:
        """Returns True if the cart is empty and False otherwise"""
        if len(self.items) == 0:
            return True
        else:
            return False