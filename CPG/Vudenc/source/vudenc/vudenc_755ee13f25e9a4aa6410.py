def get_invoiceById(id):...
sql_query = (
    'select i.transaction_date, ip.invoice_id, p.name, ip.quantity, p.price from invoice_products as ip, products as p, invoices as i where invoice_id = %s and ip.product_id = p.id and ip.invoice_id = i.id;'
    )
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query, id)
return cursor.fetchall()
