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

    def test_copy_image(self):
        '''
        Test to confirm that we are copying the image address 
        '''

        self.image.save_image()
        Image.copy_image("images1.jpg")

        self.assertEqual(self.image.image,pyperclip.paste())