from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import EmployerUserSerializer


User = get_user_model()

class EmployerUserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Employer User profile Retrieve, Update & Destroy"""

    serializer_class = EmployerUserSerializer
    queryset = User.objects.all()

    def get_object(self):
        """
        It returns the user object if the user is active and the type is 'EMPLOYER'
        :return: The user object is being returned.
        """
        return get_object_or_404(User, id=self.request.user.id, is_active=True, type='EMPLOYER')
    

