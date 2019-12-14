from django.test import TestCase
from .models import Location,category,image

class LocationTestClass(TestCase):

    def setUp(self):
        self.location= Location(name='usa')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)



