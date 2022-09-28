from django.db import models
from django.urls import reverse

# Create your models here.

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    toptap = models.CharField(max_length=200)
    established = models.IntegerField()
    image = models.ImageField(upload_to="main_app/static/uploads", default="")

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'brewery_id': self.id})