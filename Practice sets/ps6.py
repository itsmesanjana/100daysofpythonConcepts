###Library managemeant system###

class Library:
    def __init__(self):
     self.noBooks=0
     self.books=[]     
      
    def addBook(self,book):
        self.books.append(book) 
        self.noBooks=len(self.books)

    def showInfo(self):
     print(f"The library has {self.noBooks} books.The books are")
     for book in self.books:
         print(book)
    
l1=Library()
l1.addBook("Harry potter1")
l1.addBook("Harry potter2")
l1.addBook("Harry potter3")
l1.addBook("Harry potter4")
l1.addBook("Harry potter5")
l1.addBook("Harry potter6")
l1.addBook("Harry potter7")
l1.addBook("Harry potter8")
l1.showInfo()