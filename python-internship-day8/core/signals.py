from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Employer, Candidate


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'Employer':
            Employer.objects.create(user=instance, name=instance.username)
        elif instance.role == 'Candidate':
            Candidate.objects.create(user=instance)
