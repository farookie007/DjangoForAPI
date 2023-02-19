from django.test import TestCase
# Local imports
from .models import Todo

# Create your tests here.
class TodoModelTest(TestCase):
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