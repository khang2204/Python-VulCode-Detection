def get_invoice(id):...
sql_query = (
    'select t2.id as id_invoice , t2.transaction_date, sum(t3.price * t1.quantity) as montant from  invoice_products as t1 inner join invoices  as t2 on  t2.id = t1.invoice_id inner join  products  as t3 on  t3.id = t1.product_id  and t2.user_id= %s group by  t2.id, t2.transaction_date order by  t2.transaction_date DESC'
    )
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query, id)
return cursor.fetchall()
