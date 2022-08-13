from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile, Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwrags):
    if created:
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()


@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwargs):
    if instance.location:
        instance.location.delete()
