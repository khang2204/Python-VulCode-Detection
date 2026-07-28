"""ebay active listings
run from: premium report, garagsale_xml
"""
from __future__ import unicode_literals
from __future__ import print_function
import __builtin__ as builtins
import sys
import os.path
import datetime
from datetime import date
from types import MethodType
import string
import frappe
from frappe import msgprint
sys.path.insert(0, '/Users/ben/dev/ebaysdk-python/dist/ebaysdk-2.1.5-py2.7.egg'
    )
sys.path.insert(0,
    '/usr/local/lib/python2.7/dist-packages/ebaysdk-2.1.4-py2.7.egg')
sys.path.insert(0,
    '/usr/local/lib/python2.7/dist-packages/lxml-3.6.4-py2.7-linux-i686.egg')
from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading
import ugssettings
sys.path.insert(0, frappe.get_app_path('unigreenscheme'))
PATH_TO_YAML = os.path.join(os.sep, frappe.utils.get_bench_path(), 'sites',
    frappe.get_site_path(), 'ebay.yaml')
def update_sold_statusDONOTUSE():...
sql = """
    DONT DO THIS UNLESS ABSOLUTELT SURE ABOUT QTY BETTER TO DO VIA IMPORT???????
    update set it.workflow_state = 'Sold'

    select it.item_code, bin.actual_qty
    from `tabItem` it
    right join `tabBin` bin
    on bin.item_code = it.item_code

    right join `zEbayListings` el
    on el.sku = it.item_code
    where el.qty =0 and bin.actual_qty =0
    """
@frappe.whitelist()...
"""docstring"""
create_ebay_listings_table()
page = 1
listings_dict = get_myebay_selling_request(page)
pages = int(listings_dict['ActiveList']['PaginationResult'][
    'TotalNumberOfPages'])
while pages >= page:
for item in listings_dict['ActiveList']['ItemArray']['Item']:
def get_myebay_selling_request(page):...
ebay_id = item['ItemID']
page += 1
"""docstring"""
qty = int(item['QuantityAvailable'])
if pages >= page:
api_trading = Trading(config_file=PATH_TO_YAML, warnings=True, timeout=20)
print(e)
return products
sku = item['SKU']
sku = ''
curr_ebay_price = float(item['SellingStatus']['CurrentPrice']['value'])
listings_dict = get_myebay_selling_request(page)
api_request = {'ActiveList': {'Include': True, 'Pagination': {
    'EntriesPerPage': 100, 'PageNumber': page}, 'IncludeWatchCount': True},
    'DetailLevel': 'ReturnAll'}
print(e.response.dict())
curr_ex_vat = curr_ebay_price / ugssettings.VAT
api_trading.execute('GetMyeBaySelling', api_request)
hit_count = 0
products = api_trading.response.dict()
watch_count = 0
question_count = 0
site = ''
insert_ebay_listing(sku, ebay_id, qty, curr_ebay_price, site, hit_count,
    watch_count, question_count)
