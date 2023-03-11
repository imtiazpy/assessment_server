from django.urls import path

from .views import EmployerUserRetrieveUpdateDestroyAPIView

app_name = 'employers'

urlpatterns = [
    path('profile/', EmployerUserRetrieveUpdateDestroyAPIView.as_view(), name='employer-profile'),
]