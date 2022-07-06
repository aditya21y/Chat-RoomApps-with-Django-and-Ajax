from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    msg = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
#after we creating the data we need to ma migration on this project using python manage.py makemigrations
#and python manage.py migrate
#if we want to access the data we need root acout or super user in admin. before we can access the admin panel we need
# to make super user account using python manage.py createsuperuser
# after finish creating the account we need to register the data model in admin file.