from django.contrib import admin
from .models import Brewery, Specialbrew

# Register your models here.

admin.site.register(Brewery)
admin.site.register(Specialbrew)