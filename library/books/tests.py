from django.test import TestCase
from django.urls import reverse
# Local imports
from .models import Book

# Create your tests here.
class BookTests(TestCase):
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
    
    def test_book_content(self):
        self.assertEqual(self.book.title, self.book_data.get("title"))
        self.assertEqual(self.book.subtitle, self.book_data.get("subtitle"))
        self.assertEqual(self.book.author, self.book_data.get("author"))
        self.assertEqual(self.book.isbn, self.book_data.get("isbn"))
    
    def test_book_listview(self):
        response = self.client.get(reverse("books:books_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book_data.get("title"))
        self.assertTemplateUsed(response, "books/list.html")