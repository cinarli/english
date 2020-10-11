
from django.db.models import Max
from .models import Word
import random




def get_random_obj():
        max_id = Word.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            category = Word.objects.filter(pk=pk).first()
            if category:
                return category
