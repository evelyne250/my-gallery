from django.db import models
import pyperclip
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

    def update_category(self):
        '''
        method that saves categories
        '''
        self.update()
    def delete_category(self):
        '''
        method that deletes categories
        '''
        self.delete()

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
    def update_location(self):
        '''
        method that updates locations
        '''
        self.update()

    def delete_location(self):
        '''
        method that deletes locations
        '''
        self.delete()
    


class Image(models.Model):
    image = models.ImageField(upload_to='pics/')
    image_name = models.CharField(max_length=30)
    description = models.TextField()
    location= models.ForeignKey(Location)
    category = models.ForeignKey(Category, db_column='names')



    def __str__(self):

        '''
        displays images
        '''
        return self.image_name
    
    def save_image(self):
        '''
        method to save images
        '''
        return self.save()
    def delete_image(self):

        '''
        method to delete images
        '''
        return self.delete()


    def update_image(self, img):
        '''
        Method to update images
        '''
        self.update()


    @classmethod
    def copy_image(cls,image):
        image_found = Image.image(image)
        pyperclip.copy(image_found.image)
        
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__names__contains=search_term)
        return photos
