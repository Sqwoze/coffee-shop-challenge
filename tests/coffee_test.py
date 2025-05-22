import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Coffee._all.clear()
        Order._all.clear()
        Customer._all.clear()
        self.customer = Customer("Bob")
        self.coffee = Coffee("Cappuccino")

    def test_valid_name(self):
        self.assertEqual(self.coffee.name, "Cappuccino")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("Hi")
        with self.assertRaises(ValueError):
            Coffee(123)  # not a string

    def test_orders_and_customers(self):
        self.customer.create_order(self.coffee, 3.5)
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertIn(self.customer, self.coffee.customers())

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        self.customer.create_order(self.coffee, 4.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0.0)
        self.customer.create_order(self.coffee, 2.0)
        self.customer.create_order(self.coffee, 4.0)
        self.assertAlmostEqual(self.coffee.average_price(), 3.0)

if __name__ == "__main__":
    unittest.main()
