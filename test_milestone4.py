import unittest
from product import Product
from store import Store
from entry import Entry
from hash_mapping import HashMapping
from algorithms import merge_sort, quick_sort, quick_select


def make(ids):
    """Builds a list of products from a list of ids"""
    return [Product(pid, "Item " + pid, 1.0) for pid in ids]


def ids(products):
    """Returns the ids of a product list"""
    return [p.get_id() for p in products]


class TestMergeSort(unittest.TestCase):
    """Tests for merge_sort"""
    def test_empty_and_one(self):
        empty = []
        merge_sort(empty)
        self.assertEqual(empty, [])
        one = make(["P1"])
        merge_sort(one)
        self.assertEqual(ids(one), ["P1"])

    def test_reverse_order(self):
        products = make(["P5", "P4", "P3", "P2", "P1"])
        merge_sort(products)
        self.assertEqual(ids(products), ["P1", "P2", "P3", "P4", "P5"])

    def test_duplicates(self):
        products = make(["P2", "P1", "P2", "P1"])
        merge_sort(products)
        self.assertEqual(ids(products), ["P1", "P1", "P2", "P2"])

    def test_already_sorted(self):
        products = make(["P1", "P2", "P3"])
        merge_sort(products)
        self.assertEqual(ids(products), ["P1", "P2", "P3"])


class TestQuickSort(unittest.TestCase):
    """Tests for quick_sort"""
    def test_empty_and_one(self):
        empty = []
        quick_sort(empty)
        self.assertEqual(empty, [])
        one = make(["P1"])
        quick_sort(one)
        self.assertEqual(ids(one), ["P1"])

    def test_reverse_order(self):
        products = make(["P5", "P4", "P3", "P2", "P1"])
        quick_sort(products)
        self.assertEqual(ids(products), ["P1", "P2", "P3", "P4", "P5"])

    def test_duplicates(self):
        products = make(["P3", "P1", "P3", "P2", "P1"])
        quick_sort(products)
        self.assertEqual(ids(products), ["P1", "P1", "P2", "P3", "P3"])

    def test_sorts_in_place(self):
        products = make(["P3", "P1", "P2"])
        same_list = products
        quick_sort(products)
        self.assertIs(products, same_list)
        self.assertEqual(ids(same_list), ["P1", "P2", "P3"])


class TestQuickSelect(unittest.TestCase):
    """Tests for quick_select (k = 0 is the smallest)"""
    def test_first_rank(self):
        products = make(["P3", "P1", "P2"])
        self.assertEqual(quick_select(products, 0).get_id(), "P1")

    def test_middle_and_last_rank(self):
        products = make(["P5", "P2", "P4", "P1", "P3"])
        self.assertEqual(quick_select(products, 2).get_id(), "P3")
        self.assertEqual(quick_select(products, 4).get_id(), "P5")

    def test_invalid_rank(self):
        products = make(["P1", "P2"])
        self.assertIsNone(quick_select(products, -1))
        self.assertIsNone(quick_select(products, 2))
        self.assertIsNone(quick_select([], 0))

    def test_duplicates(self):
        products = make(["P2", "P1", "P2"])
        self.assertEqual(quick_select(products, 1).get_id(), "P2")
        self.assertEqual(quick_select(products, 2).get_id(), "P2")


class TestHashMapping(unittest.TestCase):
    """Tests for Entry and HashMapping"""
    def test_entry(self):
        entry = Entry("P1", "Keyboard")
        self.assertEqual(entry.key, "P1")
        self.assertEqual(entry.value, "Keyboard")

    def test_put_get_contains_len(self):
        mapping = HashMapping(size=3)
        mapping.put("P100", "Keyboard")
        mapping.put("P200", "Headphones")
        self.assertEqual(mapping.get("P100"), "Keyboard")
        self.assertIn("P200", mapping)
        self.assertNotIn("P999", mapping)
        self.assertEqual(len(mapping), 2)

    def test_update_keeps_length(self):
        mapping = HashMapping()
        mapping.put("P100", "Keyboard")
        mapping.put("P100", "Wireless Keyboard")
        self.assertEqual(mapping.get("P100"), "Wireless Keyboard")
        self.assertEqual(len(mapping), 1)

    def test_missing_key_raises(self):
        mapping = HashMapping()
        with self.assertRaises(KeyError):
            mapping.get("P999")

    def test_collisions(self):
        # one bucket forces every key to collide
        mapping = HashMapping(size=1)
        mapping.put("A", 10)
        mapping.put("D", 20)
        self.assertEqual(mapping.get("A"), 10)
        self.assertEqual(mapping.get("D"), 20)
        self.assertEqual(len(mapping), 2)

    def test_rehash_keeps_entries(self):
        mapping = HashMapping(size=2)
        for i in range(50):
            mapping.put("K" + str(i), i)
        mapping.rehash()
        self.assertEqual(len(mapping), 50)
        for i in range(50):
            self.assertEqual(mapping.get("K" + str(i)), i)


class TestStoreIntegration(unittest.TestCase):
    """Tests for the new Store methods"""
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("P300", "Mouse", 29.99))
        self.store.add_product(Product("P100", "Keyboard", 59.99))
        self.store.add_product(Product("P200", "Headphones", 39.99))

    def test_merge_sort_products(self):
        self.store.merge_sort_products()
        self.assertEqual(ids(self.store.products), ["P100", "P200", "P300"])

    def test_quick_sort_products(self):
        self.store.quick_sort_products()
        self.assertEqual(ids(self.store.products), ["P100", "P200", "P300"])

    def test_quick_select_product(self):
        self.assertEqual(self.store.quick_select_product(1).get_id(), "P200")
        self.assertIsNone(self.store.quick_select_product(3))

    def test_find_product(self):
        self.assertEqual(self.store.find_product("P100").get_name(), "Keyboard")
        self.assertIsNone(self.store.find_product("P999"))

    def test_duplicate_product_rejected(self):
        self.assertFalse(self.store.add_product(Product("P100", "Other", 1.0)))
        self.assertEqual(self.store.find_product("P100").get_name(), "Keyboard")
        self.assertEqual(len(self.store.products), 3)


if __name__ == "__main__":
    unittest.main()
