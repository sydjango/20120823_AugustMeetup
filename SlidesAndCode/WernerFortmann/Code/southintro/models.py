from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=100, null = True)
    password_salt = models.CharField(max_length=8, null = True)

    name = models.TextField()
    COLOURS=(('RED','red'),('BLUE','blue'),('OTHR','other'),)
    haircolour = models.CharField(max_length=4, choices=COLOURS, default='OTHR')
