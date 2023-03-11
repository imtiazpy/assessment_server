from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from jobseekers.models import JobSeekerProfile


User = get_user_model()

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class meta:
        model = JobSeekerProfile
        fields = (
            'id',
            'overview',
            'gender',
            'date_of_birth',
            'city',
            'country'
        )
        read_only_fields = ('id', )


class JobSeekerUserSerializer(serializers.ModelSerializer):
    """Retrieve, Update, Destroy Job seeker profile"""

    job_seeker_profile = JobSeekerProfileSerializer(many=False)
    class Meta:
        model = User
        fields = ('name', 'avatar', 'type', 'job_seeker_profile')
        read_only_fields = ('id', 'type', )

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        It updates the instance of the model with the validated_data, and then updates the
        job_seeker_profile with the job_seeker_profile data
        
        :param instance: The instance of the model that is being updated
        :param validated_data: The validated data from the serializer
        :return: The new instance of the model.
        """
        
        ModelClass = self.Meta.model
        job_seeker_profile = validated_data.pop('job_seeker_profile', {})

        ModelClass.objects.filter(id=instance.id).update(**validated_data)

        if job_seeker_profile:
            JobSeekerProfile.objects.filter(owner=instance).update(**job_seeker_profile)

        new_instance = get_object_or_404(ModelClass, id=instance.id)
        return new_instance
