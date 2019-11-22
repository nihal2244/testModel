from django.contrib import admin
from .models import User,Bills  

# Register your models here.
myModels = [User,Bills]  # iterable list
admin.site.register(myModels)