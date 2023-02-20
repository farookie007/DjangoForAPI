from django.test import TestCase
from django.contrib.auth import get_user_model
# Local imports
from .models import Post


class BlogTests(TestCase):
    user_data = {
        "username": "testuser",
        "email": "test@email.com",
        "password": "secret_password",
    }
    post_data = {
        "title": "Test title",
        "body": "Test post body",
    }

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username=cls.user_data.get("username"),
            email=cls.user_data.get("email"),
            password=cls.user_data.get("password"),
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title =cls.post_data.get("title"),
            body=cls.post_data.get("body"),
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, self.user_data.get("username"))
        self.assertEqual(self.post.title, self.post_data.get("title"))
        self.assertEqual(self.post.body, self.post_data.get("body")),
        self.assertEqual(str(self.post), self.post_data.get("title"))