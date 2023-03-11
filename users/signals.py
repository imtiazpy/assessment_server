from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from employers.models import EmployerProfile
from jobseekers.models import JobSeekerProfile

User = get_user_model()


"""
This is a signal receiver function that is triggered after a User object is saved. It checks if the created parameter is True, which means a new User instance has just been created.

If created is True, it then checks the type attribute of the User instance and creates a corresponding profile object (EmployerProfile or JobSeekerProfile) with the User instance as the owner.

This code assumes that User instances have a type attribute that indicates whether the user is an employer or a job seeker, and that EmployerProfile and JobSeekerProfile are related profile objects for these respective user types.
"""
@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        if instance.type == 'EMPLOYER':
            EmployerProfile.objects.create(owner=instance)
        elif instance.type == 'JOB_SEEKER':
            JobSeekerProfile.objects.create(owner=instance)




"""
This is a signal receiver function that is triggered when a User object is saved. It checks the type attribute of the User instance and saves the corresponding profile object (employer_profile or job_seeker_profile) based on the value of type.

This code assumes that User instances have a type attribute that indicates whether the user is an employer or a job seeker, and that employer_profile and job_seeker_profile are related profile objects for these respective user types.
"""
@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **kwargs):
    if instance.type == 'EMPLOYER':
        instance.employer_profile.save()
    elif instance.type == 'JOB_SEEKER':
        instance.job_seeker_profile.save()

