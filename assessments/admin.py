from django.contrib import admin

from .models import Assessment, AssessmentAttempt


admin.site.register(Assessment)
admin.site.register(AssessmentAttempt)

