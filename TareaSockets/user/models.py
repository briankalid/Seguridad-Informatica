from django.db import models

# Create your models here.

class user_homework(models.Model):
    name = models.CharField(max_length = 60, primary_key = True)
    pswd = models.CharField(max_length = 4) 
