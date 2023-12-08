from django.db import models
from django.contrib.auth.models import AbstractUser


class UserLog(AbstractUser):  
    phone = models.IntegerField(max_length=True,unique=True)
    email = models.EmailField(null=True, blank=True)
    



class Contacts(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    registered_user = models.BooleanField(default=False)
    spam_count = models.IntegerField(default=0)
    email = models.EmailField(null=True)







