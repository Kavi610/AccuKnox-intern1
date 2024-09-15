from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import employee

@receiver(post_save, sender=employee)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler executed.")



