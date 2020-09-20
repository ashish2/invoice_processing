from django.db import models

from basemodel.models import BaseModel

# Create your models here.

class Invoice(BaseModel):
	# Invoice File Model
	name 
	path
	type

class Customer_InvoiceFile(BaseModel):
	customer_id
	invoiceFile_id

class Vendor(BaseModel):
	name
	address

class Purchaser(BaseModel):
	name
	address

class InvoiceDetails(BaseModel):
	# Invoice Details Model
	invoicefile_id

	invoice_number
	vendor_id
	purchaser_id
	date

class LineItems(BaseModel):
	# Line Item Details model
	invoicedetails_id
	description
	quantity
	unitAmount
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




