class Customer():
    def __init__(self, name, min_length=1, max_length=15):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) < min_length:
            raise ValueError(f"Name mist be at least {min_length} characters long.")
        elif len(name) > max_length:
            raise ValueError(f"name must be at most {max_length} characters long.")
        
        self.name = name

user_input = input("Enter your name: ")

try:
    customer = Customer(user_input)
    print(f"Welcome, {customer.name}!")

except ValueError as e:
    print(f"Error: {e}")