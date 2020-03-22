from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Aggression(models.Model):
    aggression_text = models.TextField()
    time = models.DateTimeField('date occurred')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now=True)
    def __str__(self):
        return self.aggression_text