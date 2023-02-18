from django.views.generic import ListView
# local imports
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/list.html"
    context_object_name = "books"