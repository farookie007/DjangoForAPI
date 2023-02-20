from rest_framework import generics
# Local imports
from .models import Todo
from .serializers import TodoSerializer


class ListViewTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailViewTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer