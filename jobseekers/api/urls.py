from django.urls import path

from .views import JobSeekerUserRetrieveUpdateDestroyAPIView

app_name = 'jobseekers'

urlpatterns = [
    path('profile/', JobSeekerUserRetrieveUpdateDestroyAPIView.as_view(), name='job-seeker-profile'),
]