from customer import Customer
from coffee import Coffee

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Make orders
alice.create_order(latte, 3.5)
bob.create_order(latte, 4.5)
alice.create_order(espresso, 2.0)

# Print results
print(f"Alice's Coffees: {[c.name for c in alice.coffees()]}")
print(f"Latte Average Price: {latte.average_price():.2f}")
print(f"Top Latte Fan: {Customer.most_aficionado(latte).name}")