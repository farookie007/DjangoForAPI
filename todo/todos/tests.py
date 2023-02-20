from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Local imports
from .models import Todo


class TodoModelTest(APITestCase):
    """Test the `Todo` model."""
    todo_data = {
        "title": "A todo title",
        "body": "The body of the todo."
    }
    
    @classmethod
    def setUpTestData(cls):
        """Sets up a prop database object for the model."""
        cls.todo = Todo.objects.create(
            title = cls.todo_data.get("title"),
            body = cls.todo_data.get("body"),
        )
        
    def test_model_content(self):
        self.assertEqual(self.todo.title, self.todo_data.get("title"))
        self.assertEqual(self.todo.body, self.todo_data.get("body"))
        self.assertEqual(str(self.todo), self.todo_data.get("title"))

    def test_api_listview(self):
        response = self.client.get(reverse("todos:api_todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todos:api_todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo_data.get("title"))
