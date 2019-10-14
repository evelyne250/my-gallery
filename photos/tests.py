from django.test import TestCase
from .models import Category,Location,Image
import pyperclip
# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.travel= Category(names="travel")

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

    # Testing Save Method
    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_update_category(self):
        '''
        Test if  Category object can be updated.
        '''
        self.travel.save_category()
        self.category = Category.objects.filter(names = 'travel').update(names = "love")
        self.category_new = Category.objects.get(names = 'love')
        self.assertEqual(self.category_new.names,"love")


    def tearDown(self):
        '''
        Test delete category behaivour
        
        '''
        Category.objects.all().delete()
        

    def test_delete_category(self):
        '''
        Test if category can be deleted from db.
        '''
        self.travel.save_category()
        self.category = Category.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)



class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(location="kigali")

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))

    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        '''
        Test if  Location object can be updated.
        '''
        self.kigali.save_location()
        self.location = Location.objects.filter(location = 'kigali').update(location = "zanzibar")
        self.location_new = Location.objects.get(location = 'zanzibar')
        self.assertEqual(self.location_new.location,"zanzibar")

    def tearDown(self):
        '''
        Test delete location behaivour
        
        '''
        Location.objects.all().delete()
        

    def test_delete_location(self):
        '''
        Test if location can be deleted from db.
        '''
        self.kigali.save_location()
        self.location = Location.objects.get(id = 1)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating image and saving it
        self.new_image= Image(image = 'images.jpg', image_name = 'success', description ='success is needed', location ='kigali', category ='travel')
        self.new_image.save()
        # Creating category and saving it
        self.travel= Category(names = 'travel')
        self.travel.save_category()
        # Creating location and saving it
        self.kigali= Location(names = 'kigali')
        self.kigali.save_location()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    # def test_copy_image(self):
    #     '''
    #     Test to confirm that we are copying the image address 
    #     '''

    #     self.image.save_image()
    #     Image.copy_image("images1.jpg")

    #     self.assertEqual(self.image.image,pyperclip.paste())