from django.urls import path
# local imports
from .views import BookListView


app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="books_list"),
]