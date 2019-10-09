from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    names = models.CharField(max_length =30)

    def __str__(self):
        '''
        display category
        '''
        return self.names


class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        '''
        displays Locations
        '''
        return self.location

class Image(models.Model):
    # image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    location= models.ForeignKey(Location)
    category = models.ForeignKey(Category)



    def __str__(self):

        '''
        displays images
        '''
        return self.image_name