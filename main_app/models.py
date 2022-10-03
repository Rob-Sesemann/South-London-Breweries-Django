from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
VARIETY = [
    ('DIPA', 'Double Indian Pale Ale'),
    ('IPA', 'Indian Pale Ale'),
    ('PA', 'Pale Ale'),
    ('L', 'Lager'),
    ('STO', 'Stout'),
    ('WHA', 'Wheat Ale'),
    ('SIP', 'Session Indian Pale Ale'),
    ('TIP', 'Triple Indian Pale Ale'),
    ('SOUR', 'Sour ale'),
]

VARIETYCORE = [
    ('DIPA', 'Double Indian Pale Ale'),
    ('IPA', 'Indian Pale Ale'),
    ('PA', 'Pale Ale'),
    ('L', 'Lager'),
    ('STO', 'Stout'),
    ('WHA', 'Wheat Ale'),
    ('SIP', 'Session Indian Pale Ale'),
    ('TIP', 'Triple Indian Pale Ale'),
    ('SOUR', 'Sour ale'),
]

class Corebrew(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    variety = models.CharField(max_length=4, choices=VARIETYCORE, default=VARIETYCORE[0][0]) # DIPA IPA PA L STO WHA SIP TIP SOUR
    corebrewery = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('corebrews_detail', kwargs={'pk': self.id})

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    toptap = models.CharField(max_length=200)
    established = models.IntegerField()
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    corebrews = models.ManyToManyField(Corebrew)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'brewery_id': self.id})

    def __str__(self):
        return self.name
    
    def specialbrew_ready(self):
        return self.specialbrew_set.filter(date=date.today()).count() >= len(VARIETY)

class Specialbrew(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateField()
    variety = models.CharField(max_length=4, choices=VARIETY, default=VARIETY[0][0]) # DIPA IPA PA L STO WHA SIP TIP SOUR
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_variety_display()} on {self.date}"

    class Meta:
        ordering = ['date']
