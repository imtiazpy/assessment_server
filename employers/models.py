from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()

# The IndustryType class is a subclass of the TextChoices class. It has three class attributes: IT,
# INTERNET, and SOFTWARE. Each attribute has a value and a human-readable label
class IndustryType(models.TextChoices):
    IT = "IT", "Information Technology"
    INTERNET = "INTERNET", "Internet"
    SOFTWARE = "SOFTWARE", "Software"


class SizeChoices(models.TextChoices):
    micro = "1-9", "1-9"
    small = "10-49", "10-49"
    medium = "50-249", "50-249"

class EmployerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    industry_type = models.CharField(
        _('Industry Type'), 
        max_length=70, 
        choices=IndustryType.choices, 
        null=True, 
        blank=True
    )
    hq = models.CharField(
        _('Head Quarter'),
        max_length=100,
        blank=True,
        null=True
    )
    company_name = models.CharField(_('Company Name'), max_length=100, blank=True, null=True)
    company_size = models.CharField(
        _('Company Size'),
        max_length=70,
        choices=SizeChoices.choices,
        blank=True,
        null=True
    )
    description = models.TextField(_('Description'), max_length=255, blank=True, null=True)
    year_of_form = models.CharField(_('Year Of Form'), max_length=4, blank=True, null=True)

    def __str__(self):
        return f'{self.id}-{self.company_name}'