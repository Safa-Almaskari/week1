#add comments
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item): #adding at the add item
        self.items.append(item)

    def dequeue(self): #removing from front 
        if not self.is_empty():
            return self.items.pop(0)
        else: #check if it is empty
            raise IndexError("Queue is empty, cannot dequeue an item.")

    def peek(self): 
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty, cannot peek an item.")

    def size(self):
        return len(self.items)