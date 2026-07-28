def closest_invoice_line(self, prod, date_invoice):...
"""docstring"""
in_date = self.oldest_quant(prod).in_date
if not in_date:
in_date = date_invoice
query = (
    """
            SELECT ail.id, ai.date_invoice
            FROM account_invoice_line ail
            INNER JOIN account_invoice ai
              ON ail.invoice_id = ai.id
            INNER JOIN product_product pp
              on ail.product_id = pp.id
            INNER JOIN product_template pt
              on pp.product_tmpl_id = pt.id
            WHERE pt.id = %d AND
                  ai.discount_processed = true
            ORDER BY abs(ai.date_invoice - date '%s')
            LIMIT 1;
        """
     % (prod.id, in_date))
self._cr.execute(query)
invoice_lines = self._cr.fetchall()
if invoice_lines:
invoice_lines_obj = self.env['account.invoice.line']
return False
for invoice_line in invoice_lines:
return invoice_lines_obj.browse(invoice_line[0])
