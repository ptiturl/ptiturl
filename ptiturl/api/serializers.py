from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Url
        fields = ["id", "created", "owner", "uri", "url", "is_enable"]


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
