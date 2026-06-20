class StoreItem:
    def __init__(self, item, price):
        self.item = item 
        self.price = price


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them

print(f"{chips.item}\n{chips.price}")


