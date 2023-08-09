#add comments LIFO
#Think how to add/apply is_FULL??
class Stack:
    def __init__(self): #constructor, to make the stack ready
        self.items = []

    def is_empty(self): #to check if stack has no items
        return len(self.items) == 0

    def push(self, item): #to add at the top
        self.items.append(item) #append add at the end

    def pop(self):
        if not self.is_empty(): #remove at the top
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")

    def peek(self): #accesing the last element like -1
        if not self.is_empty():
            return self.items[-1]
        else:
            #raise exception handling error
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self): #return length of the list how many items
        return len(self.items)
    
    

    
    
    
        
        
        
        
        
        
        