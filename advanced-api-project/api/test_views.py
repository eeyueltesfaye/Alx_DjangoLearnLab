# api/test_views.py
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Book, Author

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post('/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(response.data['publication_year'], 2022)
        self.assertEqual(response.data['author'], self.author.id)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(f'/books/update/{self.book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')
        self.assertEqual(response.data['publication_year'], 2021)
        self.assertEqual(response.data['author'], self.author.id)

    def test_delete_book(self):
        response = self.client.delete(f'/books/delete/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify that the book is actually deleted
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # Ensure the response contains a 'results' key

    def test_get_book_detail(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['publication_year'], 2020)
        self.assertEqual(response.data['author'], self.author.id)
