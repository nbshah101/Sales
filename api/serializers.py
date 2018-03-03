from rest_framework import serializers
from .models import Sales

class SalesListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Sales
        fields = ('vin', 'make', 'model', 'year', 'price', 'buyer', 'seller')

