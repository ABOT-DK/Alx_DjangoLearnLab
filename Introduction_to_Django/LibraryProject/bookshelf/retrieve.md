
# Retrieve all Book instances

```python
from bookshelf.models import Book

# Command: Retrieve and display all attributes of the book(s) just created
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Expected output (for our single "1984" book):
# 1984 George Orwell 1949
```





# Retrieve Book instance

```python
from bookshelf.models import Book

# Command: Retrieve and display all attributes of the book with title "1984"
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected output:
# 1984 George Orwell 1949
```
