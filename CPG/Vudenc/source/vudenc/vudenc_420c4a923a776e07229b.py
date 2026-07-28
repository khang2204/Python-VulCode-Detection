def create_ebay_listings_table():...
"""docstring"""
sql = """
        create table if not exists `zEbayListings` (
        `sku` varchar(20),
        `ebay_id` varchar(38),
        `qty` integer,
        `price` decimal(18,6),
        `site` varchar(6),
        `hit_count` integer,
        `watch_count` integer,
        `question_count` integer
        )
    """
frappe.db.sql(sql, auto_commit=True)
sql2 = 'truncate table `zEbayListings` '
frappe.db.sql(sql2, auto_commit=True)
