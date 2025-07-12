# Delete Book instance

```python
from bookshelf.models import Book

# Command: Delete the book you created and confirm deletion
book = Book.objects.get(title="Nineteen Eighty‑Four")
book.delete()
print(Book.objects.all())
# Expected output:
# <QuerySet []>
# (An empty QuerySet confirming the Book instance has been deleted)
```



# Delete All Book instance

```python
from bookshelf.models import Book

# Command: Delete the book you created and confirm deletion
book = Book.objects.all().delete()
print(Book.objects.all())
# Expected output:
# <QuerySet []>
# (An empty QuerySet confirming the Book instance has been deleted)
```

