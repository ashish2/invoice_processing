from django.contrib import admin

# Register your models here.
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    # fields = ['name']
    pass


admin.site.register(Customer, CustomerAdmin)
