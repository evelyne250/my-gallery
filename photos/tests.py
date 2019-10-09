from django.test import TestCase
from .models import Category,Location,Image
from django.contrib import auth
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

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')