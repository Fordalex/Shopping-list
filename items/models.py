from django.db import models

# Create your models here.
class Item(models.Model):
    author = models.CharField(max_length=200, default='alexford')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name