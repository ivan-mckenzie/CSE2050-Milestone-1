import unittest

from product import Product
from customer import Customer
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from order import Order
from store import Store


class TestOrder(unittest.TestCase):
    """Tests for the order class"""
    def test_init_pending(self):
        customer = Customer("C1", "person1")
        order = Order("01", customer, [Product("P1", "product1", 10.0)])
        self.assertEqual(order.get_id(), "01")
        self.assertEqual(order.get_customer(), customer)
        self.assertEqual(order.get_status(), "PENDING")

    def test_items_snapshot(self):
        customer = Customer("C1", "person1")
        cart = customer.get_cart()
        cart.add_product(Product("P1", "product1", 10.0))
        order = Order("01", customer, cart.get_items())
        cart.clear()
        cart.add_product(Product("P9", "Extra", 99.0))
        self.assertEqual(len(order.get_items()), 1)
        self.assertAlmostEqual(order.calculate_total(), 10.0)


class TestLinkedList(unittest.TestCase):
    """Tests for the linked list class"""
    def test_init_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.size(), 0)
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.get_first())

    def test_add_last(self):
        ll = LinkedList()
        for num in [1, 2, 3]:
            ll.add_last(num)

        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.get_first(), 1)

    def test_add_first(self):
        ll = LinkedList()
        for num in [1, 2, 3]:
            ll.add_first(num)
        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.get_first(), 3)

    def test_remove_first(self):
        ll = LinkedList()
        ll.add_last("a")
        ll.add_last("b")
        self.assertEqual(ll.remove_first(), "a")
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.get_first(), "b")
        self.assertEqual(ll.remove_first(), "b")
        self.assertTrue(ll.is_empty())


class TestStack(unittest.TestCase):
    """Tests for the stack class"""
    def test_push_pop_lifo(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push("top")
        self.assertEqual(stack.peek(), "top")
        self.assertEqual(stack.size(), 1)

    def test_pop_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.pop())


class TestOrderQueue(unittest.TestCase):
    """Tests for the order queue class"""
    def test_enqueue_dequeue_fifo(self):
        queue = OrderQueue()
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertTrue(queue.is_empty())

    def test_peek(self):
        queue = OrderQueue()
        queue.enqueue("front")
        self.assertEqual(queue.peek(), "front")
        self.assertEqual(queue.size(), 1)

    def test_dequeue_empty(self):
        queue = OrderQueue()
        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.dequeue())


class TestStore(unittest.TestCase):
    """Tests for store checkout, processing, and history"""

    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("P100", "product1", 29.99))
        self.store.add_customer(Customer("C100", "person1"))
        self.store.add_customer(Customer("C101", "person2"))

    def test_checkout(self):
        alex = self.store.find_customer("C100")
        alex.get_cart().add_product(self.store.find_product("P100"))
        order = self.store.checkout("C100")
        self.assertIsNotNone(order)
        self.assertEqual(order.get_status(), "PENDING")
        self.assertAlmostEqual(order.calculate_total(), 29.99)
        self.assertTrue(alex.get_cart().is_empty())
        self.assertEqual(len(self.store.get_orders()), 1)

    def test_checkout_empty_cart(self):
        self.assertIsNone(self.store.checkout("C100"))

    def test_process_orders_and_history(self):
        alex = self.store.find_customer("C100")
        sam = self.store.find_customer("C101")
        alex.get_cart().add_product(self.store.find_product("P100"))
        sam.get_cart().add_product(self.store.find_product("P100"))
        first = self.store.checkout("C100")
        second = self.store.checkout("C101")

        processed = self.store.process_next_order()
        self.assertEqual(processed.get_id(), first.get_id())
        self.assertEqual(processed.get_status(), "PROCESSING")

        processed = self.store.process_next_order()
        self.assertEqual(processed.get_id(), second.get_id())

        self.assertIsNone(self.store.process_next_order())

        history = self.store.get_order_history()
        self.assertEqual(history[0].get_id(), second.get_id())
        self.assertEqual(history[1].get_id(), first.get_id())
        self.assertEqual(len(self.store.get_order_history()), 2)


if __name__ == '__main__':
    unittest.main()