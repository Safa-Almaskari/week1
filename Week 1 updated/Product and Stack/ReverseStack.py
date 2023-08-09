


def revstring(input):
        stack=Stack()
        
        for rev in input:
            stack.push(rev)
        
        reversed_string= ""
    
        while not stack.is_empty():
            reversed_string+=stack.pop()
        
        return reversed_string

print(revstring("Electronics"))
print(revstring("Accessores"))