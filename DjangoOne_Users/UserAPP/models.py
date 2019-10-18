from django.db import models
from django.contrib.auth.models import User as adminuser

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    Email = models.CharField(max_length=264,unique=True)


class UserProfileInfo(models.Model):

    user = models.OneToOneField(adminuser)

    # additional attributes
    portfolio_site= models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
