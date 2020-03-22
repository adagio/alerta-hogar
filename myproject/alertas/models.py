from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)

class Aggression(models.Model):
    aggression_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
