from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Hood(models.Model):
    hood_name = models.CharField(max_length =30)
    hood_photo = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupant_count = models.CharField(max_length =50)
    def __str__(self):
        return self.hood_name

