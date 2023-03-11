from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from employers.models import EmployerProfile


User = get_user_model()

# This class is a serializer for the EmployerProfile model
class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = (
            'id', 
            'industry_type', 
            'hq', 
            'company_name', 
            'company_size', 
            'description', 
            'year_of_form'
        )
        read_only_fields = ('id', )


class EmployerUserSerializer(serializers.ModelSerializer):
    """Retrieve, Update, Delete Employer Profile"""

    employer_profile = EmployerProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('name', 'avatar', 'type', 'employer_profile')
        read_only_fields = ('id', 'type', )

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        It updates the instance with the validated_data, and then updates the employer_profile with the
        employer_profile data
        
        :param instance: The instance of the model that is being updated
        :param validated_data: The validated data from the serializer
        :return: The new instance of the model.
        """
        
        ModelClass = self.Meta.model
        employer_profile = validated_data.pop('employer_profile', {})

        ModelClass.objects.filter(id=instance.id).update(**validated_data)

        if employer_profile:
            EmployerProfile.objects.filter(owner=instance).update(**employer_profile)

        new_instance = get_object_or_404(ModelClass, id=instance.id)

        return new_instance