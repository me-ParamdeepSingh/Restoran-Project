from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class verify_link(models.Model):
    rnd_no = models.CharField(max_length=200)
    user = models.CharField(max_length=100)


class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to="menu_items")


    def __str__(self) -> str:
        return self.item_name