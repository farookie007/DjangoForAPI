from rest_framework import serializers
# Local imports
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serializer class for the Todo model."""
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )
