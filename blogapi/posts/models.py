from django.db import models
# Local imports
from accounts.models import CustomUser


class Post(models.Model):
    class Meta:
        ordering = [
            "-created_at",
            ]
        indexes = [
            models.Index(fields=["-created_at"]),
            ]

    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation for the object.
        Returns:
            (str): the title of the object."""
        return self.title