from django.db import models

# Create your models here.

class Prize (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    points = models.IntegerField()
    image = models.ImageField()
