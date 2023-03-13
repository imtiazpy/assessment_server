from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from django_filters import rest_framework as filters

from assessments.models import Assessment
from .serializers import PublicAssessmentListSerializer, PublicAssessmentRetrieveSerializer


class PublicAssessmentListAPIView(ListAPIView):
    """List view that returns all the public Assessment"""
    serializer_class = PublicAssessmentListSerializer
    queryset = Assessment.objects.filter(is_public=True)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['type', 'difficulty', 'category']


class PublicAssessmentRetrieveSerializer(RetrieveAPIView):
    serializer_class = PublicAssessmentRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Assessment.objects.filter(slug=self.kwargs['slug'], is_public=True)
