from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    user_data = {
        'username': 'test_username',
        'email': 'test_email',
        'password': 'secret_password',
    }
    post_data = {
        'title': 'Post Title',
        'body': 'Post Body',
    }

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = cls.user_data['username'],
            email = cls.user_data['email'],
            password = cls.user_data['password'],
        )
        cls.post = Post.objects.create(
            title = cls.post_data['title'],
            body = cls.post_data['body'],
            author = cls.user,
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, self.user_data.get('username'))
        self.assertEqual(str(self.post), self.post_data.get('title'))
        self.assertEqual(self.post.title, self.post_data.get('title'))
        self.assertEqual(self.post.body, self.post_data.get('body'))
