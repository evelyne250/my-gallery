from django.test import TestCase
from .models import Category,Location,Image
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