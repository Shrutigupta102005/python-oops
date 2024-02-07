class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, nitem, qty):
        item = (nitem,qty)
        self.items.append(item)

    def remove_item(self, item_name ):
        element=self.items.index(item_name)
        self.items.remove(element)
    
    def total_item(self):
        total = 0 
        for i in self.items:
            total += i[1]
        return total
    
# creating an object for above class
    
customer1 = ShoppingCart()
customer2 = ShoppingCart()
customer1.add_items("cake",5)
customer1.add_items("colddrink",15)
customer1.add_items("ice-cream",65)
print("current item in cart:")
print(customer1.total_item())
customer1.remove_item("cake")
print(customer1.total_item())
