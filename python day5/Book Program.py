class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
        
    def discount(self,percent):
        self.price -=self.price*percent/100
        
    def __str__(self):
        return f"{self.title} costs {self.price}"
    
b = Book("Python", 570)
b.discount(10)
print(b)