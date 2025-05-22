import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Customer._all.clear()
        Order._all.clear()
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Espresso")

    def test_valid_name(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)
        with self.assertRaises(ValueError):
            self.customer.name = 123  # not a string

    def test_create_order_and_retrieve(self):
        self.customer.create_order(self.coffee1, 3.0)
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(self.customer.orders()[0].coffee, self.coffee1)

    def test_coffees_returns_unique_list(self):
        self.customer.create_order(self.coffee1, 2.5)
        self.customer.create_order(self.coffee1, 3.0)
        self.customer.create_order(self.coffee2, 4.0)
        coffees = self.customer.coffees()
        self.assertIn(self.coffee1, coffees)
        self.assertIn(self.coffee2, coffees)
        self.assertEqual(len(coffees), 2)

    def test_most_aficionado(self):
        c2 = Customer("Bob")
        self.customer.create_order(self.coffee1, 5.0)
        c2.create_order(self.coffee1, 3.0)
        self.assertEqual(Customer.most_aficionado(self.coffee1), self.customer)

if __name__ == "__main__":
    unittest.main()
