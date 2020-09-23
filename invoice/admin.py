from django.contrib import admin

# Register your models here.
from .models import *

class InvoiceAdmin(admin.ModelAdmin):
	pass
	# class Meta:
 #    	fields = '__all__'

class VendorAdmin(admin.ModelAdmin):
	pass

class PurchaserAdmin(admin.ModelAdmin):
	pass

class InvoiceDetailsAdmin(admin.ModelAdmin):
	pass

class LineItemsAdmin(admin.ModelAdmin):
	pass

class Invoice_OtherStatusAdmin(admin.ModelAdmin):
	pass

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Purchaser, PurchaserAdmin)
admin.site.register(InvoiceDetails, InvoiceDetailsAdmin)
admin.site.register(LineItems, LineItemsAdmin)
admin.site.register(Invoice_OtherStatus, Invoice_OtherStatusAdmin)
