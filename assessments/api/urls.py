from django.urls import path
from .views import PublicAssessmentListAPIView, PublicAssessmentRetrieveSerializer


urlpatterns = [
    path('public-assessments/', PublicAssessmentListAPIView.as_view(), name='public-assessments'),
    path('public/<str:slug>/', PublicAssessmentRetrieveSerializer.as_view(), name='public-assessment'),
]