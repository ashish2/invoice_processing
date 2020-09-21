from django.contrib import admin

# Register your models here.
from .models import *

class InvoiceAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Invoice, InvoiceAdmin)
