from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)
    key = models.CharField(max_length=12,editable=False)

    class Meta:
        unique_together = ('name', 'translate',)

    def __str__(self):
        return self.name
