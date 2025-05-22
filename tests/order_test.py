import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order._all.clear()
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_order_valid_creation(self):
        order = Order(self.customer, self.coffee, 3.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.0)

    def test_invalid_customer_or_coffee(self):
        with self.assertRaises(TypeError):
            Order("NotCustomer", self.coffee, 2.0)
        with self.assertRaises(TypeError):
            Order(self.customer, "NotCoffee", 2.0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)  # too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)  # too high
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "free")  # not a float

if __name__ == "__main__":
    unittest.main()
