# invoice_processing
Invoice processing


# Steps to Follow:
1. GoTo - http://localhost:8000/

2. At /basemodel/
	1. Create User : eg. User1

3. At /customer/
	1. Create Customer - attach to the User : eg. Cust1 -> User1

4. At /invoice/
	1. Upload a PDF File as Invoice - attach to Customer (Select Upload from random_files folder and upload to documents folder)
	2. Create a Vendor
	3. Create a Purchaser Object
	4. Create InvoiceDetails entry from the PDF file - attach to Invoice Object
	5. Create LineItem Entries of the Invoice from PDF - attach to Invoice
	6. Create Invoice_OtherStatus entry of the the Invoice - attach to Invoice
	7. Marking the Invoice_OtherStatus entry of the Invoice to Any (Processing,Digitzed etc) or All of the options

