from django.urls import path
# Local imports
from .views import DetailViewTodo, ListViewTodo


app_name = "todos"

urlpatterns = [
    path("<int:pk>/", DetailViewTodo.as_view(), name="api_todo_detail"),
    path("", ListViewTodo.as_view(), name="api_todo_list"),
]