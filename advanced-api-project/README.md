Manually test the views using tools like Postman or curl:
Test List View: Send a GET request to /books/ to retrieve all books.
Test Detail View: Send a GET request to /books/<id>/ to retrieve a specific book.
Test Create View: Send a POST request to /books/create/ with book data to create a new book.
Test Update View: Send a PUT or PATCH request to /books/<id>/update/ to modify a book.
Test Delete View: Send a DELETE request to /books/<id>/delete/ to delete a book.

# BookListView: Handles GET requests to retrieve all books.
# BookDetailView: Handles GET requests to retrieve a single book by its ID.
# BookCreateView: Handles POST requests to create a new book. Restricted to authenticated users.
# BookUpdateView: Handles PUT/PATCH requests to update a book. Restricted to authenticated users.
# BookDeleteView: Handles DELETE requests to remove a book. Restricted to authenticated users.




examples of how to use these features:

Filter by author: /books/?author__name=John
Search by title: /books/?search=Python
Order by publication year: /books/?ordering=publication_year