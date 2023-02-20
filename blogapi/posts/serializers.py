from rest_framework import serializers
# Local imports
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    fields = (
        "id",
        "author",
        "title",
        "body",
        "created_at",
    )
    model = Post