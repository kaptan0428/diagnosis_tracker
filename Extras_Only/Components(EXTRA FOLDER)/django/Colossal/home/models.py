from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122)
    message=models.TextField()