from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Hood(models.Model):
    hood_name = models.CharField(max_length =30)
    hood_photo = models.ImageField(upload_to = 'articles/')
    location = models.CharField(max_length = 30)
    link_hood = models.CharField(max_length = 200)
    occupant_count = models.CharField(max_length =50)


    def __str__(self):
        return self.hood_name

class Profile(models.Model):
    profile_name = models.CharField(max_length = 30)
    dpic = models.ImageField(upload_to = 'articles/')
    email_address = models.CharField(max_length = 30)
    neighborhood_id = models.ForeignKey(Hood)

    def __str__(self):
        return self.profile_name


class Business(models.Model):
    b_name =  models.CharField(max_length =30)
    b_email_address =  models.CharField(max_length =30)
    user = models.ForeignKey(User)
    neighborhood = models.ForeignKey(Hood)

    def __str__(self):
        return self.b_name
