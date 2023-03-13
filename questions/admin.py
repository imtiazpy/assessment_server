from django.contrib import admin
from .models import MCQuestion, Choice, TFQuestion, SAQuestion, Answer

admin.site.register(MCQuestion)
admin.site.register(Choice)

admin.site.register(TFQuestion)

admin.site.register(SAQuestion)
admin.site.register(Answer)