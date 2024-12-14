from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
import requests

from users.api.serializers import AvatarUploadSerializer, UserActivationSerializer


User = get_user_model()

class AvatarUploadView(generics.UpdateAPIView):
    """
    This code defines a Django REST Framework view AvatarUploadView that inherits from generics.UpdateAPIView. The view is used for updating the avatar field of a User model instance. It uses the AvatarUploadSerializer serializer class to validate and update the avatar field, and retrieves the User instance to update using the get_object method. The get_object method returns a User instance based on the current user's ID in the request, with an additional filter for is_active=True.
    """
    serializer_class = AvatarUploadSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id, is_active=True)
    
  
class UserActivationView(generics.GenericAPIView):
    """
    This class is a view for activating a user account upon clicking on the link from activation email. It sends a POST request to the activation endpoint of Djoser with the uid and token as the payload. If activation is successful, the user is redirected to a success page on the frontend.
    """

    permission_classes = [AllowAny]

    serializer_class = UserActivationSerializer

    def get(self, request, uid, token, format=None):
        payload = {'uid': uid, 'token': token}

        # activation endpoint from Djoser
        url = 'http://127.0.0.1:8000/api/v1/auth/users/activation/'

        requests.post(url, data=payload)

        # redirect to frontend upon activation successfull
        return redirect('http://localhost:3000/activation-success')