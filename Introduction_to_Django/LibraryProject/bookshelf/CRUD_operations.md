# CRUD Operations for `Book` Model

```python
from bookshelf.models import Book

# —————————
# CREATE
# —————————
# Command: Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
# Expected output:
# 1984 by George Orwell (1949)


# —————————
# RETRIEVE
# —————————
# Command: Retrieve and display all attributes of all Book instances
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
# Expected output (with only the 1984 book present):
# 1984 George Orwell 1949


# —————————
# UPDATE
# —————————
# Command: Update the title of "1984" to "Nineteen Eighty‑Four" and save
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty‑Four"
book.save()
print(book.title)
# Expected output:
# Nineteen Eighty‑Four


# —————————
# DELETE
# —————————
# Command: Delete the book and confirm deletion
book.delete()
print(Book.objects.all())
# Expected output:
# <QuerySet []>
