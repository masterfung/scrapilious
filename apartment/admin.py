from django.contrib import admin

# Register your models here.
from .models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    pass