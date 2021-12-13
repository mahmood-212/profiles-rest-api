from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name filed for testing serializer"""

    name = serializers.CharField(max_length=10)