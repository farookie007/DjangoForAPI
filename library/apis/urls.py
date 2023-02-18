from django.urls import path
# Local imports
from .views import BookAPIListView


app_name = "apis"

urlpatterns = [
    path("", BookAPIListView.as_view(), name = "api_books_list")
]