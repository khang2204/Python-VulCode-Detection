def insert_ebay_listing(sku, ebay_id, qty, price, site, hits, watches,...
"""docstring"""
sql = (
    """
    insert into `zEbayListings`
    values('{sku}', '{ebay_id}', {qty}, {price}, '{site}', {hit_count}, {watch_count}, {question_count})
    """
    .format(sku=sku, ebay_id=ebay_id, qty=qty, price=price, site=site,
    hit_count=hits, watch_count=watches, question_count=questions))
frappe.db.sql(sql, auto_commit=True)
