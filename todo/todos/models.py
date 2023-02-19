from django.db import models

# Create your models here.
class Todo(models.Model):
    """A model representing each Todo object on the database."""
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        """String represetation of the model.
        Returns:
            str: the title of the object."""
        return self.title