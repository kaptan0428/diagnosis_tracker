from django.db import models

# Create your models here.

#models.py File

class Post(models.Model):
    # title= models.CharField(max_length=300, unique=True)
    usrname = models.CharField(max_length=50,default="",primary_key=True)
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50,default="")
    bgrp = models.CharField(max_length=5,default="")
    age = models.CharField(max_length=100, default="")
    wt = models.CharField(max_length=200, default="")
    ht = models.CharField(max_length=300, default="")
    txta = models.TextField(default="")
    que1 = models.CharField(max_length=300, default="")
    que2 = models.CharField(max_length=300, default="")
    que3 = models.CharField(max_length=300, default="")
    que4 = models.CharField(max_length=300, default="")
    que6 = models.CharField(max_length=300, default="")
    que7 = models.CharField(max_length=300, default="")
    que8 = models.CharField(max_length=300, default="")
    que9 = models.CharField(max_length=300, default="")
    que10 = models.CharField(max_length=300, default="")
    que11 = models.CharField(max_length=300, default="")
    que12 = models.CharField(max_length=300, default="")
    que13 = models.CharField(max_length=300, default="")
    que14 = models.CharField(max_length=300, default="")
    que15 = models.CharField(max_length=300, default="")
    que16 = models.CharField(max_length=300, default="")
    que17 = models.CharField(max_length=300, default="")
    que18 = models.CharField(max_length=300, default="")
    que19 = models.CharField(max_length=300, default="")
    que20 = models.CharField(max_length=300, default="")
    que21 = models.CharField(max_length=300, default="")
    que22 = models.CharField(max_length=300, default="")
    que23 = models.CharField(max_length=300, default="")
    que24 = models.CharField(max_length=300, default="")
    que25 = models.CharField(max_length=300, default="")
    que26 = models.CharField(max_length=300, default="")
    que27 = models.CharField(max_length=300, default="")
    que28 = models.CharField(max_length=300, default="")
    que29 = models.CharField(max_length=300, default="")
    que30 = models.CharField(max_length=300, default="")
    que31 = models.CharField(max_length=300, default="")
    que32 = models.CharField(max_length=300, default="")
    que33 = models.CharField(max_length=300, default="")
    que34 = models.CharField(max_length=300, default="")
    que35 = models.CharField(max_length=300, default="")
    que36 = models.CharField(max_length=300, default="")
    que37 = models.CharField(max_length=300, default="")
    que38 = models.CharField(max_length=300, default="")
    que39 = models.CharField(max_length=300, default="")
    que40 = models.CharField(max_length=300, default="")
    que41 = models.CharField(max_length=300, default="")
    que42 = models.CharField(max_length=300, default="")
    que43= models.CharField(max_length=300, default="")
    que44 = models.CharField(max_length=300, default="")
    que45 = models.CharField(max_length=300, default="")
    que46= models.CharField(max_length=300, default="")


    def __str__(self):
        return self.usrname

