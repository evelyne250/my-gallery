from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    names = models.CharField(max_length =30)