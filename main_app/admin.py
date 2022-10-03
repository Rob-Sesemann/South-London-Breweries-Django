from django.contrib import admin
from .models import Brewery, Specialbrew, Corebrew

# Register your models here.

admin.site.register(Brewery)
admin.site.register(Specialbrew)
admin.site.register(Corebrew)