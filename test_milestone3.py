import unittest

from product import Product
from store import Store
from algorithms import (recursive_total_price, fewest_coins, bubble_sort,
                        selection_sort, insertion_sort, binary_search)


def make_products():
    """Returns three products in unsorted order"""
    return [Product("P300", "Mouse", 29.99),
            Product("P100", "Keyboard", 59.99),
            Product("P200", "Headphones", 39.99)]


def ids(products):
    """Returns a list of the product ids"""
    return [p.get_id() for p in products]


class TestRecursiveTotal(unittest.TestCase):
    """Tests for recursive_total_price"""
    def test_empty_list(self):
        self.assertEqual(recursive_total_price([]), 0.0)

    def test_one_product(self):
        self.assertAlmostEqual(recursive_total_price([Product("P1", "A", 5.5)]), 5.5)

    def test_multiple_products(self):
        self.assertAlmostEqual(recursive_total_price(make_products()), 129.97)


class TestFewestCoins(unittest.TestCase):
    """Tests for fewest_coins"""
    def test_amount_zero(self):
        self.assertEqual(fewest_coins([1, 5, 10], 0), 0)

    def test_exact_coin(self):
        self.assertEqual(fewest_coins([1, 5, 10], 10), 1)

    def test_mixed_coins(self):
        self.assertEqual(fewest_coins([1, 5, 10], 12), 3)

    def test_larger_amount(self):
        self.assertEqual(fewest_coins([1, 5, 10, 25], 99), 9)

    def test_impossible(self):
        self.assertEqual(fewest_coins([5, 10], 3), -1)


class TestSorting(unittest.TestCase):
    """Tests for the three sorting algorithms"""
    def test_bubble_sort(self):
        products = make_products()
        bubble_sort(products)
        self.assertEqual(ids(products), ["P100", "P200", "P300"])

    def test_selection_sort(self):
        products = make_products()
        selection_sort(products)
        self.assertEqual(ids(products), ["P100", "P200", "P300"])

    def test_insertion_sort(self):
        products = make_products()
        insertion_sort(products)
        self.assertEqual(ids(products), ["P100", "P200", "P300"])

    def test_already_sorted(self):
        for sorter in [bubble_sort, selection_sort, insertion_sort]:
            products = [Product("P1", "A", 1.0), Product("P2", "B", 2.0), Product("P3", "C", 3.0)]
            sorter(products)
            self.assertEqual(ids(products), ["P1", "P2", "P3"])

    def test_reverse_sorted(self):
        for sorter in [bubble_sort, selection_sort, insertion_sort]:
            products = [Product("P3", "C", 3.0), Product("P2", "B", 2.0), Product("P1", "A", 1.0)]
            sorter(products)
            self.assertEqual(ids(products), ["P1", "P2", "P3"])

    def test_empty_and_one(self):
        for sorter in [bubble_sort, selection_sort, insertion_sort]:
            empty = []
            sorter(empty)
            self.assertEqual(empty, [])
            one = [Product("P1", "A", 1.0)]
            sorter(one)
            self.assertEqual(ids(one), ["P1"])


class TestBinarySearch(unittest.TestCase):
    """Tests for binary_search on a sorted list"""
    def setUp(self):
        self.products = make_products()
        insertion_sort(self.products)

    def test_first_item(self):
        self.assertEqual(binary_search(self.products, "P100"), 0)

    def test_middle_item(self):
        self.assertEqual(binary_search(self.products, "P200"), 1)

    def test_last_item(self):
        self.assertEqual(binary_search(self.products, "P300"), 2)

    def test_not_found(self):
        self.assertEqual(binary_search(self.products, "P999"), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], "P100"), -1)


class TestStoreMilestone3(unittest.TestCase):
    """Integration tests for the new Store methods"""
    def setUp(self):
        self.store = Store()
        for product in make_products():
            self.store.add_product(product)

    def test_sort_products(self):
        for method in [self.store.bubble_sort_products,
                       self.store.selection_sort_products,
                       self.store.insertion_sort_products]:
            method()
            self.assertEqual(ids(self.store.products), ["P100", "P200", "P300"])

    def test_binary_search_product(self):
        self.store.insertion_sort_products()
        self.assertEqual(self.store.binary_search_product("P200").get_name(), "Headphones")
        self.assertIsNone(self.store.binary_search_product("P999"))

    def test_catalog_total(self):
        self.assertAlmostEqual(self.store.recursive_catalog_total(), 129.97)

    def test_catalog_total_empty(self):
        self.assertEqual(Store().recursive_catalog_total(), 0.0)

    def test_calculate_change(self):
        self.assertEqual(self.store.calculate_change([1, 5, 10], 12), 3)
        self.assertEqual(self.store.calculate_change([1, 5, 10], 0), 0)


if __name__ == '__main__':
    unittest.main()
