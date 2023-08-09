"""
Create Product class
each product has name, category, and price--> instance variable
class is able to return  discription of product--> method
for each product be able to compute discount of a given amount
(compute price after discount of amount%)
"""
class Product:
    #constructor method
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    def get_price(self):
        return self.price
    
    def set(self, newName):
        self.name = newName
    def set(self, newCategory):
        self.name = newcategory
    def set(self, newPrice):
        self.name = newPrice
        
     
    def descrip(self):
        return f"Product's name is {self.name} category {self.category} price is {self.price} OMR"
    
    #how much discount after the amount?
    def discount(self,amount):
        #self.result price is updated
        #mutotur method it changed the value
        self.price = self.price - (self.price * amount/100)
        if self.category == "Electronics":
            self.price += 10
        























