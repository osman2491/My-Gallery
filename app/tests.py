from django.test import TestCase
from .models import Location,category,image

class imageTestClass(TestCase):

    def setUp(self):
        self.images= image(image_name = 'usa',image_discription='usa is a great country')

    def test_instance(self):
        self.assertTrue(isinstance(self.images,image))



