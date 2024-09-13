class Library:
    def __init__(self):
        self.noOfBook=0
        self.books=[]
    def addABook(self, book):
        self.books.append(book)
        
    def info(self):
        print(f"No of book are {len(self.books)} books. Books are: {self.books}")

l1=Library()

l1.addABook('pythons')
l1.info()