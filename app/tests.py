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

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

     def test_update_location(self):
        new_location = 'paris'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='paris')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Category(name='travel')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='my photo', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))



