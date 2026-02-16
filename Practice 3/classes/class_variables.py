class Item:
    total_items = 0
    
    def __init__(self, name):
        self.name = name
        Item.total_items += 1
        print(f"Created: {self.name} (Total: {Item.total_items})")
    
    def remove(self):
        Item.total_items -= 1
        print(f"Removed: {self.name} (Remaining: {Item.total_items})")

a = Item("Apple")
b = Item("Banana")
print(f"Total: {Item.total_items}")
a.remove()
print(f"Total: {Item.total_items}")