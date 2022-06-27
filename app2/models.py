from curses import ACS_GEQUAL
from django.db import models

# Create your models here.
class Main(models.Model):
     name = models.CharField(max_length=255)
     decr = models.TextField(max_length=500)
     age = models.IntegerField()
     gender = models.CharField(max_length=255)


     def __str__(self):
         return self.name


