from django.contrib import admin
from .models import User,Bills,BillRelation

# Register your models here.
myModels = [User,Bills,BillRelation]  # iterable list
admin.site.register(myModels)