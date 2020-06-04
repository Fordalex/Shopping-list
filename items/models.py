from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

class Item(models.Model):
    author = models.CharField(max_length=200, default='alexford')
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name