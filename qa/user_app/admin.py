from django.contrib import admin
from .models import AnsweredQuestion,ActiveQuestion

admin.site.register(AnsweredQuestion)
admin.site.register(ActiveQuestion)
