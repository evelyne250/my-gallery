from django.db import models

# Create your models here.

class Category(models.Model):
    names = models.CharField(max_length =30)

    def __str__(self):
        '''
        display category
        '''
        return self.names

    def save_category(self):
        '''
        method that saves categories
        '''
        self.save()

class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        '''
        displays Locations
        '''
        return self.location
    

    def save_location(self):
        '''
        method to save image
        '''
        return self.save()


class Image(models.Model):
    image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    location= models.ForeignKey(Location)
    category = models.ForeignKey(Category)



    def __str__(self):

        '''
        displays images
        '''
        return self.image_name
    
    def save_image(self):
        '''
        method to save image
        '''
        return self.save()
    @classmethod
    def pictures(cls):

        '''
        method to get all images 
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
