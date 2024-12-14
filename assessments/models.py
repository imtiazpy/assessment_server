from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from .enums import AssessmentDifficulties, AssessmentTypes, AssessmentCategories

User = get_user_model()

class Assessment(models.Model):
    """Model definition for Assessment"""

    title = models.CharField(_('Title'), max_length=100, blank=False, null=False)
    description = models.TextField(_('Description'), max_length=500, blank=True, null=True)
    type = models.CharField(
        _('Type'), 
        choices=AssessmentTypes.choices, 
        max_length=50,
        blank=False, 
        null=False
    )
    difficulty = models.CharField(
        _('Difficulty'), 
        choices=AssessmentDifficulties.choices,
        max_length=50,
        blank=False, 
        null=False
    )
    category = models.CharField(
        _('Category'),
        choices=AssessmentCategories.choices,
        max_length=50,
        blank=False,
        null=False
    )
    slug = models.SlugField(_('Slug'), max_length=6, blank=True, null=True)
    # default duration of 10 minutes
    duration = models.PositiveIntegerField(_('Duration'), default=600)
    is_public = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments')

    def save(self, *args, **kwargs):
        """
        If the object doesn't have a slug, generate a random string and check if any other objects have the same slug. If they do, generate a new random string and check again. If they don't, save the object
        """
        if not self.slug:
            self.slug = get_random_string(6)
            duplicate_slug = True
            while duplicate_slug:
                other_obj_with_same_slug = type(self).objects.filter(slug=self.slug)
                if len(other_obj_with_same_slug) > 0:
                    self.slug = get_random_string(6)
                else:
                    duplicate_slug = False
        
        super(Assessment, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}-{self.title}'
    


class AssessmentAttempt(models.Model):
    """Model definition for Assessment attempts"""

    job_seeker = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING, 
        related_name='jobseeker_attempts'
    )
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.DO_NOTHING,
        related_name='assessment_attempts'
    )
    score = models.IntegerField(_('Score'), blank=True, null=True)
    start_time = models.DateTimeField(_('Start Time'), auto_now_add=True)
    end_time = models.DateTimeField(_('End Time'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.end_time is None:
            self.end_time = timezone.now()
        super().save(*args, **kwargs)
    
    @property
    def get_remaining_time(self):
        """
        It returns the number of seconds remaining in the Assessment, or 0 if the assessment is over
        :return: The remaining time in seconds.
        """
        elapsed_time = timezone.now() - self.start_time
        remaining_time = self.duration - elapsed_time.total_seconds()
        return max(0, int(remaining_time))
    
    def __str__(self):
        return f'{self.id}-{self.assessment.title}'
