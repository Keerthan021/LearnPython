class Product:
    def __init__(self, price):
        self._price = price  # convention: underscore for internal use

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

# Usage
p = Product(100)
print(p.price)     # calls the getter
p.price = 200      # calls the setter
del p.price        # calls the deleter
