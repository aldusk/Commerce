from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.TextField()
    

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishes")
    listing_id = models.ForeignKey("Listing", on_delete=models.CASCADE)


class Comment(models.Model):
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Biding(models.Model):
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bidden")
    activity = models.BooleanField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField()


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    descripte_me = models.TextField()
    photo = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")