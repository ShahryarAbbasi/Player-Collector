from django.contrib import admin
from .models import Player # import the Artist model from models.py
# Register your models here.

admin.site.register(Player) # this line will add the model to the admin panel