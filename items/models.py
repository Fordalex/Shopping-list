from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    author = models.CharField(max_length=200, default='alexford')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Item(models.Model):
    author = models.CharField(max_length=200, default='alexford')
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    author = models.CharField(max_length=200, default='alexford')
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="owner", null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return self.current_user.username