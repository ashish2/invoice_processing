# invoice_processing
Invoice processing

### Command 1: Create an Invoice Object
curl 'http://localhost:8000/invoice/invoice/' \
  -X 'POST' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 23259' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://localhost:8000' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryTpWtBEzvGPFAi8w5' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Referer: http://localhost:8000/invoice/invoice/' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Cookie: sessionid=0rsez3zv0m2d9f8veck8o7e1f7jossvn; csrftoken=WOLCnMsnxR0nIkmQTiwWfAZKKqDYvJNGTzKqLN9CO1j7ZJFIX9RQJrHXxa6DExBg; tabstyle=html-tab' \
  --compressed



# Steps to Follow:
	Create User
	Create Customer - attach to the User
	Upload a PDF File as Invoice (Above: Command 1) - attach to Customer
	Create a Vendor
	Create a Purchaser Object
	Create InvoiceDetails entry from the PDF file - attach to Invoice Object
	Create LineItem Entries of the Invoice from PDF - attach to Invoice
	Create Invoice_OtherStatus entry of the the Invoice - attach to Invoice

