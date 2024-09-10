from rest_framework import serializers


class HomeSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
