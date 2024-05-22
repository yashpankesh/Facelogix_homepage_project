# models.py
from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # You might want to use a more secure way to store passwords
    class Meta:
        app_label = 'facelogix2'
    def __str__(self):
        return self.username
