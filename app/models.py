from django.db import models


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class category(models.Model):
    categorys = models.CharField(max_length=30)

    def __str__(self):
        return self.categorys

class image(models.Model):
    image_name = models.CharField(max_length=30)
    image_discription = models.CharField(max_length=30)
    Location = models.ForeignKey(Location)
    category = models.ForeignKey(category)
    

    def __str__(self):
        return self.image_name
    




