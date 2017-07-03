from django.contrib import admin

# Register your models here.
from .models import Gensetengine, Genset

admin.site.register(Gensetengine)
admin.site.register(Genset)
