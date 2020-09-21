from django.db import models

from basemodel.models import BaseModel
from customer.models import Customer

# Create your models here.

class Invoice(BaseModel):
	# Invoice File Model
	name 
	path
	type
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Customer_InvoiceFile(BaseModel):
# 	customer_id
# 	invoiceFile_id

class Vendor(BaseModel):
	name
	address

class Purchaser(BaseModel):
	name
	address

class InvoiceDetails(BaseModel):
	# Invoice Details Model
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

	invoice_number
	vendor_id
	purchaser_id
	date

class LineItems(BaseModel):
	# Line Item Details model
	invoicedetails_id
	description
	quantity
	unit_amount
	total

class InvoiceDetails_LineItems(BaseModel):
	invoice_id
	lineItems_id

class Invoice_OtherStatus(BaseModel):
	invoice_id
	processing = Boolean
	processed = Boolean
	digitizing = Boolean
	digitized = Boolean




