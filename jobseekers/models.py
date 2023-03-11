from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model


User = get_user_model()

class Gender(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'


class JobSeekerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    overview = models.TextField(_('Overview'), max_length=255, blank=True, null=True)
    gender = models.IntegerField(_('Gender'), choices=Gender.choices, blank=True, null=True)
    data_of_birth = models.DateField(_('Date of Birth'), blank=True, null=True)
    city = models.CharField(_('City'), max_length=50, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.id}-{self.owner.get_full_name()}'