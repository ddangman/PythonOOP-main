from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

item6 = Item("InitialItem", 750)

# Setting an Attribute
item6.name = "RenamedItem"

# Getting an Attribute
print(item6.name)