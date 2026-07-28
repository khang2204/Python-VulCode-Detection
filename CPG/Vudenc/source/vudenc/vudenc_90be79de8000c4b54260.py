def create_invoice_products(userId, products, invoiceId):...
invoice_products_values = UsersRepository.create_invoice_products_values_query(
    invoiceId, products)
print('Result:')
print(invoice_products_values)
sql_query = f"""
            INSERT INTO {INVOICE_PRODUCTS_TABLE} (invoice_id, product_id, quantity)
            VALUES {invoice_products_values}
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query)
connection.commit()
return 'Ok'
