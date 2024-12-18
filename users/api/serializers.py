from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer


User = get_user_model()

class UserSerializer(UserCreateSerializer):
    """
    This code defines a customized serializer class UserSerializer that inherits from djoser.serializers.UserCreateSerializer. It includes the type field and is referenced in the settings.py file under the DJOSER object. The serializer will not be used directly in any views, but rather with djoser endpoints for handling user registration requests.
    """
    class Meta:
        model = User
        fields = ('id', 'type', 'name', 'email', 'password')


class AvatarUploadSerializer(ModelSerializer):
    """
    This code defines a serializer class AvatarUploadSerializer used for uploading an avatar image for an existing User model instance. It has a single field for avatar, and can be used with a Django REST Framework view to handle avatar upload requests.
    """
    class Meta:
        model = User
        fields = ('avatar', )
        

# "This class is a serializer that takes a uid and token and validates them."
class UserActivationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()