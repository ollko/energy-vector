from django.contrib import admin

# Register your models here.
from .models import Marka, Certificate

admin.site.register(Marka)
admin.site.register(Certificate)