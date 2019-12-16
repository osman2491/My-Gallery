from django.db import models


class Location(models.Model):
    location = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()

    @classmethod
    def get_location(cls):
        place = cls.objects.all()
        return place

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update_category()

    def __str__(self):
        return self.category

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    img_location = models.ForeignKey(Location)
    img_category = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'welcome/')


    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    @classmethod
    def img_details(cls):
        image = cls.objects.all()
        return image

    @classmethod
    def search_by_image_name(cls,search_term):
        image = cls.objects.filter(image_name__icontains=search_term)
        return image
    

    def __str__(self):
        return self.image_name
    




