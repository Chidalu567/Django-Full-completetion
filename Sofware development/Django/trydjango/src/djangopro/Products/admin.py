from django.contrib import admin
from .models import Product #import product class from models.py

# Register your models here.
#I want to register my model i the APP admin and store value in database
admin.site.register(Product); # register a model in the app admin
