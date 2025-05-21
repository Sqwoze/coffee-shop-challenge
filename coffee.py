from dataclasses import dataclass

@dataclass(frozen=True)
class Coffee:
    _name: str

    def __post_init__(self):
        if not isinstance(self._name, str):
            raise ValueError("Name must be a string.")
        if len(self._name) < 3:
            raise ValueError("Name must be at least 3 characters long.")

    @property
    def name(self):
        return self._name

coffee_input = input("Enter The type of coffee you'd like: ")

try:
    coffee = Coffee(coffee_input)
    print(f"You chose a {coffee_input}")

        
except ValueError as e:
    print(f"Error: {e}")