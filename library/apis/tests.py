from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# Local imports
from books.models import Book

# Create your tests here.
class APITests(APITestCase):
    book_data = {
    "title": "A good title",
    "subtitle": "An excellent subtitle",
    "author": "Tom Christie",
    "isbn": "1234567890123"
    }
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = cls.book_data.get("title"),
            subtitle = cls.book_data.get("subtitle"),
            author = cls.book_data.get("author"),
            isbn = cls.book_data.get("isbn"),
        )
    
    def test_api_listview(self):
        resp = self.client.get(reverse("apis:api_books_list"))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(resp, self.book)