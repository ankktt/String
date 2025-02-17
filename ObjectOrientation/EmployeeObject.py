class Employee:
    company_name = 'code' #class Based Variable
    def __init__(self,name, age, desig):
        self.name = name
        self.age = age
        self.desig = desig

    def login(self, time):
        print(f'{self.name} loggrd in at{time}')
    
    def logout(self,time):
        print(f'{self.name} loggedout at {time}')
    
    def work(self, hours):
        print(f'{self.name} worked for {hours}')
    
    def getDetails(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Desiganation:', self.desig)

e1 = Employee('Ak', 24,'SDE')
e2 = Employee('pk', 25, 'Manager')
e3 = Employee('RK', 26, 'Developer')

e1.getDetails()
e2.getDetails()
e3.getDetails()








class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        if self.is_available:
            status = "Available" 
        else:
            status = "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

    def mark_borrowed(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} has been marked as borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

book = Book("1984", "George Orwell")
book.display_info()
book.mark_borrowed()
book.display_info()



class Product:
    def __init__(self,p_name,price,stock):
        self.p_name = p_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f'Product Name: {self.p_name}, Price: {self.price}, Stock: {self.stock}')
    
    def update_price(self,newPrice):
        self.price = newPrice
        print(f'Updating price to {newPrice}...')
        print(f'New Price: {newPrice}')
    
    def update_stock(self, newstock):
        self.stock = newstock
        print(f'Updating stock to {newstock}...')
        print(f'New Stock: {newstock}')

p_name = input()
price = float(input())
stock = int(input())
newprice = float(input())
newstock = int(input())

p1 = Product(p_name,price,stock)
p1.display_info()
p1.update_price(newprice)
p1.update_stock(newstock)