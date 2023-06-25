from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class verify_link(models.Model):
    rnd_no = models.CharField(max_length=200)
    user = models.CharField(max_length=100)