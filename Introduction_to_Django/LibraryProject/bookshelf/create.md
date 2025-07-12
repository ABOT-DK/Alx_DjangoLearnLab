# Create a Book instance

```python
from bookshelf.models import Book

# Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected output: A new Book object is created and assigned to `book`, e.g.:
# <Book: 1984 by George Orwell (1949)>
