# How to create a class:
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        ##  Actions to execute
        # Append new instance of Item to all list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# How to create an instance of a class
item1 = Item("Phone", 100)

# Calling methods from instances of a class:
# print(item1.calculate_total_price(item1.price, item1.quantity))


# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item("Laptop", 1000)

# Calling methods from instances of a class: 
# print(item2.calculate_total_price(item2.price, item2.quantity))

print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = .5
item2.apply_discount()
print(item2.price)


item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)