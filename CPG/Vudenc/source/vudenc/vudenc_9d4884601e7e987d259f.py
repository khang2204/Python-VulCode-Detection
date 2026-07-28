def create_invoice_products_values_query(invoiceId, products):...
invoice_products_values = ''
for product in products['products']:
invoice_products_values += '('
invoice_products_values = invoice_products_values[:-1]
invoice_products_values += str(invoiceId['id'])
return invoice_products_values
invoice_products_values += ','
invoice_products_values += str(product['product']['productId'])
invoice_products_values += ','
invoice_products_values += str(product['product']['quantity'])
invoice_products_values += '),'
