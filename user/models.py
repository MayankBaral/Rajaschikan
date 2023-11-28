from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10,null=True)  # You can adjust the max length as needed
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    zipcode = models.CharField(max_length=6,null=True)
    

    def __str__(self):
        return self.users.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(users=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()