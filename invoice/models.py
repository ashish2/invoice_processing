from django.db import models

from basemodel.models import BaseModel
from customer.models import Customer

# Create your models here.
class Invoice(BaseModel):
	# Invoice File Model
	name = models.CharField(max_length=256)
	path = models.FileField(upload_to='documents/%Y/%m/%d/')
	extension = models.CharField(max_length=32)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Customer_InvoiceFile(BaseModel):
# 	customer_id
# 	invoiceFile_id

class Vendor(BaseModel):
	name = models.CharField(max_length=256)
	address = models.TextField()

class Purchaser(BaseModel):
	name = models.CharField(max_length=256)
	address = models.TextField()

class InvoiceDetails(BaseModel):
	# Invoice Details Model
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
	number = models.IntegerField() # Invoice Number
	vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	purchaser_id = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
	date =  models.DateTimeField() # Invoice Date

class LineItems(BaseModel):
	# Line Item Details model
	invoicedetails = models.ForeignKey(InvoiceDetails, on_delete=models.CASCADE)
	description = models.CharField(max_length=256)
	quantity = models.FloatField()
	unit_amount = models.FloatField()
	total = models.FloatField()

# class InvoiceDetails_LineItems(BaseModel):
# 	invoice_id
# 	lineItems_id

class Invoice_OtherStatus(BaseModel):
	invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
	processing = models.BooleanField()
	processed =  models.BooleanField()
	digitizing = models.BooleanField()
	digitized = models.BooleanField()

