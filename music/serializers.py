from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.Serializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")