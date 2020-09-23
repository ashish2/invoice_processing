# invoice_processing
Invoice processing


# Steps to Follow:
GoTo - http://localhost:8000/

At /basemodel/
	Create User : eg. User1

At /customer/
	Create Customer - attach to the User : eg. Cust1 -> User1

At /invoice/
	Upload a PDF File as Invoice - attach to Customer (Select Upload from random_files folder and upload to documents folder)
	Create a Vendor
	Create a Purchaser Object
	Create InvoiceDetails entry from the PDF file - attach to Invoice Object
	Create LineItem Entries of the Invoice from PDF - attach to Invoice
	Create Invoice_OtherStatus entry of the the Invoice - attach to Invoice

