# Delete Operation

```python
from bookshelf.models import Book

# Assuming you have already created a book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())

```
