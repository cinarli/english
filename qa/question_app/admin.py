from django.contrib import admin
from .models import Word

admin.site.register(Word)

class WordAdmin(admin.ModelAdmin):
    exclude = ('key',)
