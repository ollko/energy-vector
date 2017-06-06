from django.contrib import admin

# Register your models here.
from .models import Marka, Certificate, Otziv

admin.site.register(Marka)
admin.site.register(Certificate)
admin.site.register(Otziv)