from django.db import models
from question_app.models import Word
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class AnsweredQuestion(models.Model):

    answer=models.ForeignKey(Word, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    true_count = models.IntegerField(default=0)
    false_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} | {self.answer.name}  ( True {self.true_count} / False {self.false_count} )"


class ActiveQuestion(models.Model):
    answer = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} | {self.answer.name}"

