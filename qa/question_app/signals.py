from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Word
from .utils import get_random_key

@receiver(pre_save,sender=Word)
def create_key(sender, instance, *args, **kwargs):
    instance.key = get_random_key()
    
