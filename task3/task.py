class Book:
  def __init__(self, name, count_pages, price):
    self.Name = name
    self.Count_pages = count_pages
    self.Price = price
    
  def info(self):
    return print(f"""
Book name: {self.Name}, Book pages: {self.Count_pages}, Book price: {self.Price}$""")
    
  def info1(self):
    """Bu funksiya barcha kitoblarni sahifalarini o'rtacha narxini qaytaradi"""  
    
    return print(f"""
Book name: {self.Name}, Book pages: {self.Count_pages}, Book price: {self.Price}$: Book pages price: {self.Price // self.Count_pages}$""")
  
  def info2(self):
    """Bu funksiya "Programming" so'zi ishtirok etgan barcha kitoblarni narxini 2 barobarga oshiradi"""  
    a = "Programming"
    lst = [self.Name]
    for i in lst:
      b = i.split()
      for j in b:
        if j == "Programming":
          return print(f""""{a}" bo'lgan kitoblarning narxi {self.Price} 2 barobar oshirildi {self.Price * 2}""")
  
k1 = Book("O'tkan kunlar", 50, 50000)
k2 = Book("Programming study", 70, 25000)    
k3 = Book("Mehrobdan chayon", 123, 30000)    
k4 = Book("Programming ", 260, 45000)    
k5 = Book("Hamsa", 150, 80000)  

lst = [k1, k2, k3, k4, k5]

for i in lst:
  i.info()
print("\n")  

print("Task1\n")
for i in lst:
  i.info1()    
  print()
  
print("Task2:\n") 
for i in lst:
  i.info2()  